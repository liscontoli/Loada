from typing import List, Optional
from pydantic import BaseModel

class NegotiationRequest(BaseModel):
    pickup_location: str
    dropoff_location: str
    load_type: str
    weight: int
    distance: int
    broker_offer: float
    previous_offers: List[float] = []


class NegotiationResponse(BaseModel):
    analysis: str
    suggested_counter_offer: float
    ai_reply: str
