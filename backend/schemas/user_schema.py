from pydantic import BaseModel, EmailStr

# Signup Schema
class UserSignupRequest(BaseModel):
    email: EmailStr
    password: str
    name: str

# Login Schema
class UserLoginRequest(BaseModel):
    email: EmailStr
    password: str

# Password Recovery Schemas
class ForgotPasswordRequest(BaseModel):
    email: EmailStr

class ConfirmPasswordRequest(BaseModel):
    email: EmailStr
    new_password: str
    confirmation_code: str