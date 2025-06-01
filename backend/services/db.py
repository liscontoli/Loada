import boto3
from config import AWS_REGION

dynamodb = boto3.resource('dynamodb', region_name=AWS_REGION)
