import boto3
from botocore.exceptions import ClientError
from config import AWS_REGION, COGNITO_CLIENT_ID

client = boto3.client("cognito-idp", region_name=AWS_REGION)

def forgot_password(email: str):
    try:
        client.forgot_password(
            ClientId=COGNITO_CLIENT_ID,
            Username=email
        )
        return {"message": "Password reset code sent to your email."}
    except ClientError as e:
        return {"error": str(e)}

def confirm_reset_password(email: str, confirmation_code: str, new_password: str):
    try:
        client.confirm_forgot_password(
            ClientId=COGNITO_CLIENT_ID,
            Username=email,
            ConfirmationCode=confirmation_code,
            Password=new_password
        )
        return {"message": "Password reset successful."}
    except ClientError as e:
        return {"error": str(e)}
