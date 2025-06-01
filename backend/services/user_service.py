from services.db import dynamodb
from boto3.dynamodb.conditions import Key
from config import DYNAMODB_USERS_TABLE

users_table = dynamodb.Table(DYNAMODB_USERS_TABLE)

def create_user(email: str, name: str):
    response = users_table.put_item(Item={"email": email, "name": name})
    return response

def get_user(email: str):
    response = users_table.get_item(Key={"email": email})
    return response.get("Item")

def update_user_name(email: str, new_name: str):
    response = users_table.update_item(
        Key={"email": email},
        UpdateExpression="SET #n = :name",
        ExpressionAttributeNames={"#n": "name"},
        ExpressionAttributeValues={":name": new_name}
    )
    return response
