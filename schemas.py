from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List, Optional

class SkillCreate(BaseModel):
    subject: str
    stability_factor: Optional[float] = 7.0

class SkillResponse(BaseModel):
    id: int
    subject: str
    stability_factor: float
    last_studied_at: datetime
    retention_score: Optional[float] = None

    class Config:
        from_attributes = True

class StudentCreate(BaseModel):
    name: str
    email: str

class StudentResponse(BaseModel):
    id: int
    name: str
    email: str
    credits: int
    skills: List[SkillResponse] = []

    class Config:
        from_attributes = True

class PeerMatchResponse(BaseModel):
    peer_id: int
    peer_name: str
    peer_email: str
    can_teach: str
    can_learn: str
    match_score: float
