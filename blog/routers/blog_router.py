from fastapi import APIRouter , Depends , status , HTTPException
from typing import List
from sqlalchemy.orm import Session
from .. import schemas, database, models , OAuth2
get_db = database.get_db
from .. repository import blog_repository 


router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)


                  #Read / for getting all data/to fetch all blog entries from the database

@router.get('/', response_model= List[schemas.ShowBlog] )
def show_all(db: Session = Depends(get_db) , current_user: schemas.User = Depends(OAuth2.get_current_user)):
     return blog_repository.show_all(db)  #  ----->  def show_all(db: Session):
                                        #            blogs = db.query(models.Blog).all()
                                       #             return blogs






                            # creation / for storing data
@router.post('/' , status_code = status.HTTP_201_CREATED )
def create(request : schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(OAuth2.get_current_user)): 
    return blog_repository.create(request,db)
    
    




                             #deletion
@router.delete('/{id}' , status_code= status.HTTP_204_NO_CONTENT)
def delete(id:int, db: Session = Depends(get_db) , current_user: schemas.User = Depends(OAuth2.get_current_user)):
    return blog_repository.delete(id,db)
    
   


                                #updation
@router.put('/{id}', status_code= status.HTTP_202_ACCEPTED )
def update(id:int, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(OAuth2.get_current_user)):
    return blog_repository.update(id,request,db)
     



         #for getting data through id / single blog entry from the database by its id
       
@router.get('/{id}' , status_code = 200 , response_model=schemas.ShowBlog )
# The Function Receives the Path Parameter:
def show_data_by_id(id:int,  db: Session = Depends(get_db) , current_user: schemas.User = Depends(OAuth2.get_current_user)):
    return blog_repository.show_data_by_id(id,db)
    
    