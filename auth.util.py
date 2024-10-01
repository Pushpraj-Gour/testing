from fastapi import HTTPException, Security, Depends
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
import requests

# Use the /token endpoint for getting tokens
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

async def bearer_auth(token: Annotated[str, Depends(oauth2_scheme)]):
    
    # Replace this with actual validation logic against the token provider
    # You can call your own service or validate the JWT directly
    
    validation_url = f"https://your-token-validation-endpoint?token={token}"
    response = requests.get(validation_url)

    if response.status_code != 200:
        raise HTTPException(status_code=403, detail="Invalid token or token expired")

    # Extract user ID or other relevant data from the token validation response
    token_info = response.json()
    user_id = token_info.get("sub")  # 'sub' typically contains the user ID in a JWT

    if not user_id:
        raise HTTPException(status_code=403, detail="Invalid token or token does not contain user ID")

    return user_id  # Return user ID or any relevant information from the token
