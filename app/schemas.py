from pydantic import BaseModel
from typing import Optional

class BusinessBase(BaseModel):
    business_name: str
    owner_name: str
    email: str
    phone_number: str
    recruitment_batch: str
    domain: str
    description: Optional[str] = None
    contact_info: Optional[str] = None
    logo: Optional[str] = None

class BusinessCreate(BusinessBase):
    pass

class Business(BusinessBase):
    id: int

    class Config:
        from_attributes = True
        
class BusinessUpdate(BaseModel):
    business_name: Optional[str] = None
    owner_name: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None
    recruitment_batch: Optional[str] = None
    domain: Optional[str] = None
    description: Optional[str] = None
    contact_info: Optional[str] = None
    logo: Optional[str] = None