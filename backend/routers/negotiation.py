from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import List
from services.negotiation_ai import negotiate_load
from dependencies.auth import verify_token

router = APIRouter(prefix="/negotiate", tags=["AI Negotiation"])

class NegotiationRequest(BaseModel):
    pickup_location: str
    dropoff_location: str
    load_type: str
    weight: float
    distance: float
    broker_offer: float
    previous_offers: List[float]

@router.post("/")
def negotiate(request: NegotiationRequest, claims: dict = Depends(verify_token)):
    result = negotiate_load(
        pickup_location=request.pickup_location,
        dropoff_location=request.dropoff_location,
        load_type=request.load_type,
        weight=request.weight,
        distance=request.distance,
        broker_offer=request.broker_offer,
        previous_offers=request.previous_offers,
    )
    return result