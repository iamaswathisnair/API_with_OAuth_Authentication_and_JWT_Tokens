from fastapi import APIRouter , Depends , status , HTTPException
from typing import List
from sqlalchemy.orm import Session
from .. import schemas, database, models
get_db = database.get_db
from passlib.context import CryptContext



router = APIRouter(
    prefix="/user",
    tags =['Users']
)




#User creation and hashed password
                                    
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
@router.post('/', response_model = schemas.ShowUser)
def create_user(request : schemas.User , db: Session = Depends(get_db)):
    hashedPassword = pwd_context.hash(request.Password)
    new_user = models.User_model(Name=request.Name, Email=request.Email , Password=hashedPassword) 
    db.add(new_user)  
    db.commit()      
    db.refresh(new_user)  
    return new_user

    


                                    # view/show user by id  
@router.get('/{id}' , response_model=schemas.ShowUser)

# The Function Receives the Path Parameter:

def show_user_by_id(id : int , db: Session = Depends(get_db) ):
    user = db.query(models.User_model).filter(models.User_model.id == id).first()
    
    
    # creating custome status code according to need / conditions .
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND , detail =f" User with the id {id} is not available" )
    #    response.status_code = status.HTTP_404_NOT_FOUND
    #    return {'detail' : f"Blog with the id {id} is not available "}
       
    return user















