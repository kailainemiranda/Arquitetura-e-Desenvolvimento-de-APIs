from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import datetime

from .database import engine, Base, get_db
from . import models, schemas, algorithm

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="MindP2P API",
    description="Motor de Micro-Aprendizagem P2P baseado na Curva de Ebbinghaus.",
    version="1.0.0"
)

@app.post("/students/", response_model=schemas.StudentResponse, status_code=status.HTTP_201_CREATED)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    db_student = db.query(models.Student).filter(models.Student.email == student.email).first()
    if db_student:
        raise HTTPException(status_code=400, detail="E-mail já cadastrado.")
    
    new_student = models.Student(name=student.name, email=student.email)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

@app.post("/students/{student_id}/skills/", response_model=schemas.SkillResponse)
def add_skill(student_id: int, skill: schemas.SkillCreate, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Aluno não encontrado.")
    
    new_skill = models.StudentSkill(
        student_id=student_id,
        subject=skill.subject.lower(),
        stability_factor=skill.stability_factor,
        last_studied_at=datetime.datetime.utcnow()
    )
    db.add(new_skill)
    db.commit()
    db.refresh(new_skill)
    
    new_skill.retention_score = algorithm.calculate_retention(new_skill.last_studied_at, new_skill.stability_factor)
    return new_skill

@app.get("/students/{student_id}/retention/", response_model=List[schemas.SkillResponse])
def get_student_retention(student_id: int, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Aluno não encontrado.")
    
    results = []
    for skill in student.skills:
        retention = algorithm.calculate_retention(skill.last_studied_at, skill.stability_factor)
        skill_dict = schemas.SkillResponse(
            id=skill.id,
            subject=skill.subject,
            stability_factor=skill.stability_factor,
            last_studied_at=skill.last_studied_at,
            retention_score=retention
        )
        results.append(skill_dict)
    return results

@app.get("/students/{student_id}/matches/", response_model=List[schemas.PeerMatchResponse])
def find_peer_matches(student_id: int, db: Session = Depends(get_db)):
    target_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not target_student:
        raise HTTPException(status_code=404, detail="Aluno não encontrado.")

    target_retentions = {
        s.subject: algorithm.calculate_retention(s.last_studied_at, s.stability_factor)
        for s in target_student.skills
    }

    all_other_students = db.query(models.Student).filter(models.Student.id != student_id).all()
    matches = []

    for other in all_other_students:
        other_retentions = {
            s.subject: algorithm.calculate_retention(s.last_studied_at, s.stability_factor)
            for s in other.skills
        }

        for subj_target, ret_target in target_retentions.items():
            if subj_target in other_retentions:
                ret_other = other_retentions[subj_target]

                # Match 1: O outro aluno pode ensinar (retenção alta vs baixa)
                if ret_other > 70.0 and ret_target < 40.0:
                    matches.append(schemas.PeerMatchResponse(
                        peer_id=other.id,
                        peer_name=other.name,
                        peer_email=other.email,
                        can_teach=subj_target,
                        can_learn="N/A",
                        match_score=round(ret_other - ret_target, 2)
                    ))

    return matches
