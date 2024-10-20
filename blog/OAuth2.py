from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends , HTTPException , status
from sqlalchemy.orm import Session
from . import  JWT_token



# Dependency to Get the Current User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
def get_current_user(token: str = Depends(oauth2_scheme)): #The token is a string, This parameter expects a JWT token

# 1. Extracts the JWT token from the request.

    credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
    )
# 2. Decodes the token to verify its validity.
    return JWT_token.verify_token(token , credentials_exception)     
  
    

# 3. Retrieves the user from the database based on the token.
   