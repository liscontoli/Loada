from fastapi import APIRouter, Depends, HTTPException
from dependencies.auth import get_current_user
from services.load_logic import calculate_load_costs
from pydantic import BaseModel
from schemas.load_schema import LoadCalculationRequest

router = APIRouter(prefix="/load", tags=["Load"])


@router.post("/calculate")
def calculate_load(
    request: LoadCalculationRequest,
    user_id: str = Depends(get_current_user)
):
    return calculate_load_costs(request.model_dump(), user_id)

@router.get("/history")
def get_load_history(user_id: str = Depends(get_current_user)):
    from services.history_service import get_user_history
    return get_user_history(user_id)
