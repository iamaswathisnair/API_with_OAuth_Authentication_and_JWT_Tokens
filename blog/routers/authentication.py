from fastapi import APIRouter , Depends , status , HTTPException
from .. import schemas , database, models
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from .. JWT_token import create_access_token

# Password context for hashing and verification
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Function to verify the password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


router = APIRouter(
    tags =['Authentication']
)

@router.post('/login')
def login(request:schemas.Login , db: Session = Depends(database.get_db)):
    
    # Retrieve the user by email
    user = db.query(models.User_model).filter(models.User_model.Email  == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials")

    if not verify_password(request.password, user.Password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect password")
        
    access_token = create_access_token(data={"sub": user.Email})
    return{"access_token": access_token, "token_type":"bearer"}

