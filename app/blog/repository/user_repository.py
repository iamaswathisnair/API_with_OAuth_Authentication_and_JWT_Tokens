from fastapi import  status , HTTPException
from sqlalchemy.orm import Session
from blog import schemas, models
from passlib.context import CryptContext





#User creation and hashed password

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def create_user(request : schemas.User , db: Session):
    hashedPassword = pwd_context.hash(request.Password)
    new_user = models.User_model(Name=request.Name, Email=request.Email , Password=hashedPassword) 
    db.add(new_user)  
    db.commit()      
    db.refresh(new_user)  
    return new_user



                              # view/show user by id  

def show_user_by_id(id : int , db: Session):
    user = db.query(models.User_model).filter(models.User_model.id == id).first()
    
    
    # creating custome status code according to need / conditions .
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND , detail =f" User with the id {id} is not available" )
    #    response.status_code = status.HTTP_404_NOT_FOUND
    #    return {'detail' : f"Blog with the id {id} is not available "}
       
    return user
















