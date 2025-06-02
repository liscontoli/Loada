from pydantic import BaseModel
from typing import Optional
from datetime import datetime, timezone
from uuid import uuid4
from decimal import Decimal
import boto3
from config import DYNAMODB_HISTORY_TABLE, AWS_REGION
from boto3.dynamodb.conditions import Key


# Setup DynamoDB
dynamodb = boto3.resource("dynamodb", region_name=AWS_REGION)
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

def convert_floats_to_decimal(obj):
    if isinstance(obj, float):
        return Decimal(str(obj))
    elif isinstance(obj, dict):
        return {k: convert_floats_to_decimal(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_floats_to_decimal(item) for item in obj]
    else:
        return obj

def save_history_entry(user_id: str, data: dict):
    now = datetime.now(timezone.utc).isoformat()
    entry = {
        "id": str(uuid4()),
        "user_id": user_id,
        "timestamp": now,  # <-- Sort key required by DynamoDB table
        "pickup_location": data["pickup_location"],
        "dropoff_location": data["dropoff_location"],
        "load_miles": Decimal(str(data["load_miles"])),
        "deadhead_miles": Decimal(str(data["deadhead_miles"])),
        "total_miles": Decimal(str(data["total_miles"])),
        "fuel_cost": Decimal(str(data["fuel_cost"])),
        "broker_offer": Decimal(str(data["broker_offer"])),
        "market_rate": Decimal(str(data["market_rate"])),
        "profitability_analysis": data["profitability_analysis"],
        "created_at": now
    }

    table.put_item(Item=entry)
    return entry

def get_history_by_user(user_id: str):
    response = table.query(
        KeyConditionExpression=Key("user_id").eq(user_id)
    )
    return response.get("Items", [])