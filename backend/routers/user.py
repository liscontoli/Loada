from fastapi import APIRouter, Depends
from dependencies.auth import verify_token
from services.user_service import get_user as get_user_by_email
from pydantic import BaseModel
from services.user_service import update_user_name

router = APIRouter(prefix="/user", tags=["User"])

@router.get("/profile")
def get_profile(claims: dict = Depends(verify_token)):
    email = claims.get("email")
    user = get_user_by_email(email)
    if user:
        return user
    return {"error": "User not found in database."}

class UserUpdate(BaseModel):
    name: str

@router.put("/profile")
def update_profile(update: UserUpdate, claims: dict = Depends(verify_token)):
    email = claims.get("email")
    update_user_name(email, update.name)
    return {"message": "User profile updated successfully ✅"}