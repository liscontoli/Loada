import boto3
from boto3.dynamodb.conditions import Key
from decimal import Decimal
from typing import List
from config import AWS_REGION, DYNAMODB_HISTORY_TABLE

# Use the region and table name from config
dynamodb = boto3.resource("dynamodb", region_name=AWS_REGION)

def get_user_history(user_id: str) -> List[dict]:
    table = dynamodb.Table(DYNAMODB_HISTORY_TABLE)

    response = table.query(
        KeyConditionExpression=Key("user_id").eq(user_id)
    )

    items = response.get("Items", [])

    # Convert Decimals to floats for JSON serialization
    for item in items:
        for key, value in item.items():
            if isinstance(value, Decimal):
                item[key] = float(value)

    return items
