from pydantic import BaseModel, EmailStr

class PersonalSettingsCreate(BaseModel):
    name: str
    email: EmailStr

class PersonalSettingsResponse(BaseModel):
    name: str
    email: EmailStr