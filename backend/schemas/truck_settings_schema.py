from pydantic import BaseModel
from typing import Optional

class TruckSettingsRequest(BaseModel):
    truck_type: str
    mpg: float
    fuel_type: str

class TruckSettingsResponse(TruckSettingsRequest):
    user_id: str
    created_at: str