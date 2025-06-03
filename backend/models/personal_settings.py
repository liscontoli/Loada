import boto3
from config import AWS_REGION, DYNAMODB_PERSONAL_SETTINGS_TABLE
from uuid import uuid4

dynamodb = boto3.resource("dynamodb", region_name=AWS_REGION)
table = dynamodb.Table(DYNAMODB_PERSONAL_SETTINGS_TABLE)

def create_or_update_personal_settings(user_id: str, data: dict):
    item = {
        "user_id": user_id,
        "name": data["name"],
        "email": data["email"]
    }
    table.put_item(Item=item)
    return item

def get_personal_settings(user_id: str):
    response = table.get_item(Key={"user_id": user_id})
    return response.get("Item")