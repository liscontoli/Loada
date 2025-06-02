from fastapi import APIRouter, Depends, HTTPException, status
from dependencies.auth import get_current_user
from services.load_logic import calculate_load_costs
from schemas.load_schema import LoadCalculationRequest, LoadSaveRequest
from models.history import save_history_entry
from services.history_service import get_user_history

router = APIRouter(prefix="/load", tags=["Load"])

@router.post("/calculate")
def calculate_load(
    request: LoadCalculationRequest,
    user_id: str = Depends(get_current_user)
):
    return calculate_load_costs(request.model_dump(), user_id)

@router.get("/history")
def get_load_history(user_id: str = Depends(get_current_user)):
    return get_user_history(user_id)

@router.post("/save", status_code=status.HTTP_201_CREATED)
def save_load_to_history(
    request: LoadSaveRequest,
    user: dict = Depends(get_current_user)
):
    try:
        data = request.model_dump()
        saved_entry = save_history_entry(user_id=user["sub"], data=data)
        return {"message": "Load saved successfully", "id": saved_entry["id"]}
    except Exception as e:
        print(f"❌ Failed to save load history: {e}")
        raise HTTPException(status_code=500, detail="Failed to save load history")