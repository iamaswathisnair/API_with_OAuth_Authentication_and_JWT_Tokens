from fastapi import APIRouter , Depends 
from sqlalchemy.orm import Session
from blog import schemas, database
get_db = database.get_db
from blog. repository import user_repository




router = APIRouter(
    prefix="/user",
    tags =['Users']
)




#User creation and hashed password
                                    
@router.post('/', response_model = schemas.ShowUser)
def create_user(request : schemas.User , db: Session = Depends(get_db)):
    return user_repository.create_user(request,db)

    


                                # view/show user by id  
@router.get('/{id}' , response_model=schemas.ShowUser)

# The Function Receives the Path Parameter:

def show_user_by_id(id : int , db: Session = Depends(get_db) ):
    return user_repository.show_user_by_id(id,db)
    
   















