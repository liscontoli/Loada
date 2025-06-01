import boto3
from botocore.exceptions import ClientError
from config import COGNITO_USER_POOL_ID, COGNITO_CLIENT_ID, AWS_REGION

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
        return {"message": "Signup successful. Please confirm the code sent to your email."}
    except ClientError as e:
        return {"error": str(e)}

def confirm_user_signup(email: str, code: str):
    try:
        response = client.confirm_sign_up(
            ClientId=COGNITO_CLIENT_ID,
            Username=email,
            ConfirmationCode=code
        )
        return {"message": "User confirmed successfully"}
    except ClientError as e:
        return {"error": str(e)}

def login_user(email: str, password: str):
    try:
        response = client.initiate_auth(
            ClientId=COGNITO_CLIENT_ID,
            AuthFlow="USER_PASSWORD_AUTH",
            AuthParameters={
                "USERNAME": email,
                "PASSWORD": password
            }
        )
        return {"token": response["AuthenticationResult"]["IdToken"]}
    except ClientError as e:
        return {"error": str(e)}