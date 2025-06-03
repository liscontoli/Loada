from pydantic import BaseModel
from uuid import uuid4
from datetime import datetime
import boto3
from config import DYNAMODB_TRUCK_SETTINGS_TABLE, AWS_REGION

# Setup DynamoDB connection
dynamodb = boto3.resource("dynamodb", region_name=AWS_REGION)
table = dynamodb.Table(DYNAMODB_TRUCK_SETTINGS_TABLE)

class TruckSettings(BaseModel):
    user_id: str
    truck_type: str
    mpg: float
    fuel_type: str
    created_at: str = datetime.utcnow().isoformat()

def save_truck_settings(data: TruckSettings):
    table.put_item(Item=data.model_dump())
    return data

def get_truck_settings(user_id: str):
    response = table.get_item(Key={"user_id": user_id})
    return response.get("Item", None)

def update_truck_settings(user_id: str, update_data: dict):
    update_expression = "SET " + ", ".join(f"{k}=:{k}" for k in update_data)
    expression_values = {f":{k}": v for k, v in update_data.items()}
    table.update_item(
        Key={"user_id": user_id},
        UpdateExpression=update_expression,
        ExpressionAttributeValues=expression_values
    )