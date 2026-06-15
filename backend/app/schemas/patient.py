from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class PatientBase(BaseModel):
    name: str
    email: EmailStr
    phone: str
    medical_history: Optional[str] = None

class PatientCreate(PatientBase):
    pass

class Patient(PatientBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]
    
    class Config:
        from_attributes = True
