from datetime import datetime
from uuid import UUID
from typing import List, Optional
from pydantic import BaseModel


class PatientEncounterSchema(BaseModel):
    """
    An encounter with a given patient.
    """
    age: Optional[int]
    arrival_method: str
    arrival_date: datetime
    arrival_time: datetime
    chief_complaints: str
    comment: str
    departure_time: Optional[datetime]
    departure_date: Optional[datetime]
    departure_dest: Optional[str]
    document_num: str
    gender: Optional[str]
    handover_from: Optional[str]
    handover_too: str
    location: str
    on_shift: bool
    patient_rfid: Optional[str]
    qr_code: Optional[str]
    triage_acuity: str

    class Config:
        orm_mode = True

class PatientEncounterResponseSchema(PatientEncounterSchema):
    """
    The patient encounter response schema.
    """
    # document uuid is created server-side when a document is created
    patient_encounter_uuid: Optional[UUID]

    class Config:
        orm_mode = True
