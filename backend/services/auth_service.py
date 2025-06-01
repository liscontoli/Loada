import boto3
from botocore.exceptions import ClientError
from config import AWS_REGION, COGNITO_CLIENT_ID
from services.user_service import create_user


client = boto3.client("cognito-idp", region_name=AWS_REGION)

def sign_up_user(email: str, password: str, name: str):
    try:
        response = client.sign_up(
            ClientId=COGNITO_CLIENT_ID,
            Username=email,
            Password=password,
            UserAttributes=[
                {"Name": "email", "Value": email},
                {"Name": "name", "Value": name}
            ]
        )

        # Save user in DynamoDB
        create_user(email=email, name=name)

        return {"message": "User registered. Please check your email to confirm."}
    except ClientError as e:
        return {"error": str(e)}



def login_user(email: str, password: str):
    try:
        response = client.initiate_auth(
            AuthFlow="USER_PASSWORD_AUTH",
            AuthParameters={
                "USERNAME": email,
                "PASSWORD": password
            },
            ClientId=COGNITO_CLIENT_ID
        )
        return {
            "access_token": response["AuthenticationResult"]["AccessToken"],
            "id_token": response["AuthenticationResult"]["IdToken"],
            "refresh_token": response["AuthenticationResult"]["RefreshToken"],
            "expires_in": response["AuthenticationResult"]["ExpiresIn"],
            "token_type": response["AuthenticationResult"]["TokenType"]
        }
    except ClientError as e:
        return {"error": str(e)}

