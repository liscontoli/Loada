from pydantic import BaseModel
from typing import List, Optional

class HistoryResponse(BaseModel):
    id: str
    pickup_location: str
    dropoff_location: str
    load_miles: float
    deadhead_miles: float
    total_miles: float
    fuel_cost: float
    broker_offer: float
    market_rate: float
    profitability_analysis: str
    created_at: str
