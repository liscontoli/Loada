from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.auth_service import sign_up_user, login_user
from schemas.user_schema import UserSignupRequest, UserLoginRequest, ConfirmPasswordRequest

router = APIRouter(prefix="/auth", tags=["Auth"])

class UserCredentials(BaseModel):
    email: str
    password: str
    name: str

@router.post("/signup")
def signup(user: UserCredentials):
    result = sign_up_user(user.email, user.password, user.name)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result


@router.post("/login")
def login(user: UserLoginRequest):
    result = login_user(user)
    if "error" in result:
        raise HTTPException(status_code=401, detail=result["error"])
    return result
