from fastapi import APIRouter, Depends
from dependencies.auth import verify_token
from services.history_service import get_user_history
from schemas.history_schema import HistoryResponse

router = APIRouter(prefix="/history", tags=["History"])

@router.get("/", response_model=list[HistoryResponse])
def fetch_history(claims: dict = Depends(verify_token)):
    user_id = claims.get("sub")  # Cognito user ID
    return get_user_history(user_id)
