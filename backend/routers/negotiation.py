from fastapi import APIRouter, Depends
from pydantic import BaseModel
from dependencies.auth import verify_token
from services.negotiation_ai import negotiate_load

router = APIRouter(prefix="/negotiate", tags=["Negotiation"])

class LoadDetails(BaseModel):
    pickup_location: str
    dropoff_location: str
    load_type: str
    weight: float
    distance: float
    broker_offer: float
    previous_offers: list[float] = []

@router.post("/")
def negotiate(load: LoadDetails, claims: dict = Depends(verify_token)):
    result = negotiate_load(
        pickup_location=load.pickup_location,
        dropoff_location=load.dropoff_location,
        load_type=load.load_type,
        weight=load.weight,
        distance=load.distance,
        broker_offer=load.broker_offer,
        previous_offers=load.previous_offers
    )
    return result
