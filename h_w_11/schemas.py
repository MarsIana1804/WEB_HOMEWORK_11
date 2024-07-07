from pydantic import BaseModel, EmailStr, constr
from typing import Optional
from datetime import date


    
class ContactBase(BaseModel):
    first_name: Optional[constr(min_length=1, max_length=100)] = None
    last_name: Optional[constr(min_length=1, max_length=100)] = None
    email: Optional[EmailStr] = None
    phone_number: Optional[constr(min_length=10, max_length=15)] = None
    birth_date: Optional[constr(min_length=10, max_length=10)] = None
    additional_info: Optional[str] = None



class ContactCreate(ContactBase):
    first_name: str
    last_name: str
    email: str
    phone_number: str
    birth_date: str
    additional_info: str

class ContactUpdate(ContactBase):
    pass

class Contact(ContactBase):
    id: int

    class Config:
        orm_mode: True