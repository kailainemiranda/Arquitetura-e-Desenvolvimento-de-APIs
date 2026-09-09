import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    credits = Column(Integer, default=10)

    skills = relationship("StudentSkill", back_populates="student")

class StudentSkill(Base):
    __tablename__ = "student_skills"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    subject = Column(String, nullable=False)
    stability_factor = Column(Float, default=7.0)  # Força da memória em dias
    last_studied_at = Column(DateTime, default=datetime.datetime.utcnow)

    student = relationship("Student", back_populates="skills")
