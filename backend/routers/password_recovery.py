from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.password_reset import forgot_password, confirm_reset_password

router = APIRouter(prefix="/password", tags=["Password Recovery"])

class ForgotPasswordRequest(BaseModel):
    email: str

class ConfirmPasswordRequest(BaseModel):
    email: str
    code: str
    new_password: str

@router.post("/forgot")
def forgot(req: ForgotPasswordRequest):
    result = forgot_password(req.email)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result

@router.post("/reset")
def reset(req: ConfirmPasswordRequest):
    result = confirm_reset_password(req.email, req.code, req.new_password)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result
