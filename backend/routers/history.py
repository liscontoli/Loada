from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from dependencies.auth import get_current_user
from schemas.load_schema import LoadHistoryResponse
from services.history_service import get_user_history
from typing import List

router = APIRouter(prefix="/load",tags=["Load History"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


@router.get("/history", response_model=List[LoadHistoryResponse])
def fetch_user_history(current_user: dict = Depends(get_current_user)):
    user_id = current_user["sub"]
    return get_user_history(user_id)