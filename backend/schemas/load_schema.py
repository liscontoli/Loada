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
    previous_offers: Optional[List[float]] = []