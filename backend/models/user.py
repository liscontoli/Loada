from pydantic import BaseModel
from uuid import uuid4
from datetime import datetime
import boto3
from config import DYNAMODB_USERS_TABLE

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(DYNAMODB_USERS_TABLE)

class User(BaseModel):
    id: str
    name: str
    email: str
    created_at: str

def create_user(name: str, email: str):
    user = User(
        id=str(uuid4()),
        name=name,
        email=email,
        created_at=datetime.utcnow().isoformat()
    )
    table.put_item(Item=user.dict())
    return user

def get_user_by_id(user_id: str):
    response = table.get_item(Key={"id": user_id})
    return response.get("Item")
