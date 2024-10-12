from fastapi import FastAPI , Depends , status , Response , HTTPException
from . import schemas , models
from .database import engine , SessionLocal ,get_db
from sqlalchemy.orm import Session
from typing import List
from passlib.context import CryptContext
from . routers import  blog_router
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


app = FastAPI()


models.Base.metadata.create_all(engine)

# Include the blog router
app.include_router(blog_router.router)  # The 'prefix' is optional but adds clarity to the URL

# Now all blog routes will be available under the /api path.



       
       
       
       


              






                                    
   





                            #User creation and hashed password
                                    
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
@app.post('/user', response_model = schemas.ShowUser,tags=['user'])
def create_user(request : schemas.User , db: Session = Depends(get_db)):
    hashedPassword = pwd_context.hash(request.Password)
    new_user = models.User_model(Name=request.Name, Email=request.Email , Password=hashedPassword) 
    db.add(new_user)  
    db.commit()      
    db.refresh(new_user)  
    return new_user

    


                                    # view/show user by id  
@app.get('/user/{id}' , response_model=schemas.ShowUser,tags=['user'])

# The Function Receives the Path Parameter:

def show_user_by_id(id : int , db: Session = Depends(get_db) ):
    user = db.query(models.User_model).filter(models.User_model.id == id).first()
    
    
    # creating custome status code according to need / conditions .
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND , detail =f" User with the id {id} is not available" )
    #    response.status_code = status.HTTP_404_NOT_FOUND
    #    return {'detail' : f"Blog with the id {id} is not available "}
       
    return user















