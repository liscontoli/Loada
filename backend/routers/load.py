from fastapi import APIRouter, Depends, HTTPException
from dependencies.auth import verify_token
from services.load_logic import calculate_load_costs
from pydantic import BaseModel
from schemas.load_schema import LoadCalculationRequest

router = APIRouter(prefix="/load", tags=["Load"])

class LoadInput(BaseModel):
    current_lat: float
    current_lng: float
    pickup_location: str
    dropoff_location: str
    truck_mpg: float
    load_weight: float
    load_miles: float
    deadhead_miles: float
    load_type: str
    broker_offer: float

@router.post("/calculate")
def calculate_load(
    request: LoadCalculationRequest,
    user_id: str = Depends(verify_token)
):
    return calculate_load_costs(request.model_dump(), user_id)