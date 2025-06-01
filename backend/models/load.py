from services.db import dynamodb
from config import DYNAMODB_LOADS_TABLE

loads_table = dynamodb.Table(DYNAMODB_LOADS_TABLE)
