from fastapi import Depends, HTTPException, status
from fastapi.security import APIKeyHeader
import requests
from jose import JWTError, jwt, jwk
from jose.utils import base64url_decode
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

oauth2_scheme = APIKeyHeader(name="Authorization")

# Load AWS Cognito configuration from environment
COGNITO_REGION = os.getenv("COGNITO_REGION")
COGNITO_USERPOOL_ID = os.getenv("COGNITO_USERPOOL_ID")
COGNITO_APP_CLIENT_ID = os.getenv("COGNITO_APP_CLIENT_ID")

# JWKS URL
COGNITO_KEYS_URL = f"https://cognito-idp.{COGNITO_REGION}.amazonaws.com/{COGNITO_USERPOOL_ID}/.well-known/jwks.json"

def fetch_jwks():
    try:
        response = requests.get(COGNITO_KEYS_URL)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to fetch JWKS keys: {str(e)}"
        )

# Load keys with error handling
jwks = fetch_jwks()

def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        headers = jwt.get_unverified_header(token)
        kid = headers['kid']
        key_index = -1
        for i, key in enumerate(jwks['keys']):
            if key['kid'] == kid:
                key_index = i
                break
        if key_index == -1:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Public key not found.")

        public_key = jwk.construct(jwks['keys'][key_index])
        message, encoded_signature = str(token).rsplit('.', 1)
        decoded_signature = base64url_decode(encoded_signature.encode('utf-8'))

        if not public_key.verify(message.encode("utf8"), decoded_signature):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Signature verification failed.")

        claims = jwt.get_unverified_claims(token)

        # Debug print
        print("Decoded Claims:", claims)

        if claims.get('client_id') != COGNITO_APP_CLIENT_ID:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token was not issued for this app client."
            )

        return claims

    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token.")
