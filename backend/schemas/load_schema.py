from pydantic import BaseModel
from typing import List, Optional

class LoadCalculationRequest(BaseModel):
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
    previous_offers: List[float] = []

class LoadHistoryResponse(BaseModel):
    pickup: str
    dropoff: str
    load_type: str
    weight: float
    total_miles: float
    fuel_cost: float
    broker_offer: float
    market_rate: float
    counter_offer: float

class LoadSaveRequest(BaseModel):
    pickup_location: str
    dropoff_location: str
    load_type: str
    load_weight: float
    load_miles: float
    deadhead_miles: float
    total_miles: float
    fuel_cost: float
    broker_offer: float
    market_rate: float
    profitability_analysis: str
    counter_offer: Optional[float] = None  # Optional in case negotiation not used