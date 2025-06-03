from typing import List, Optional
from pydantic import BaseModel

class NegotiationRequest(BaseModel):
    pickup_location: str
    dropoff_location: str
    load_type: str
    weight: int
    distance: int
    broker_offer: float
    market_rate: float  
    previous_offers: List[float] = []
    countered_amount: Optional[float] = None  # Optional when broker counters

class NegotiationResponse(BaseModel):
    analysis: str
    suggested_counter_offer: float
    ai_reply: str