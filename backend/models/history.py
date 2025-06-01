from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from uuid import uuid4
import boto3
from config import DYNAMODB_HISTORY_TABLE, AWS_REGION

dynamodb = boto3.resource('dynamodb', region_name=AWS_REGION)
table = dynamodb.Table(DYNAMODB_HISTORY_TABLE)

class HistoryEntry(BaseModel):
    id: str
    user_id: str
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

def save_history_entry(user_id: str, data: dict):
    entry = HistoryEntry(
        id=str(uuid4()),
        user_id=user_id,
        pickup_location=data["pickup_location"],
        dropoff_location=data["dropoff_location"],
        load_miles=data["load_miles"],
        deadhead_miles=data["deadhead_miles"],
        total_miles=data["total_miles"],
        fuel_cost=data["fuel_cost"],
        broker_offer=data["broker_offer"],
        market_rate=data["market_rate"],
        profitability_analysis=data["profitability_analysis"],
        created_at=datetime.utcnow().isoformat()
    )
    table.put_item(Item=entry.dict())
    return entry
