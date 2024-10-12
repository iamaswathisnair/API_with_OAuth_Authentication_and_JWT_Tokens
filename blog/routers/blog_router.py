from fastapi import APIRouter , Depends , status , HTTPException
from typing import List
from sqlalchemy.orm import Session
from .. import schemas, database, models
get_db = database.get_db


router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)


                  #Read / for getting all data/to fetch all blog entries from the database

@router.get('/', response_model= List[schemas.ShowBlog] )
def show_all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs





                            # creation / for storing data
@router.post('/' , status_code = status.HTTP_201_CREATED )
def create(request : schemas.Blog, db: Session = Depends(get_db)): 
    new_blog = models.Blog(Title=request.Title, Body=request.Body,user_id =1) 
    db.add(new_blog)  # Using the session to add the new blog
    db.commit()       # Committing the transaction (saving to the database)
    db.refresh(new_blog)  # Refreshes the instance with the latest data from the database
    return new_blog





                                    #deletion
@router.delete('/{id}' , status_code= status.HTTP_204_NO_CONTENT)
def delete(id , db: Session = Depends(get_db)):
   
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not available")
    # If the blog exists, proceed to update it
    blog.delete(synchronize_session = False)
    db.commit()       # Committing the transaction (saving to the database)
    # return 'Done'
   





                                    #updation
@router.put('/{id}', status_code= status.HTTP_202_ACCEPTED )
def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
    # First, check if the blog exists
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
   
    # If no blog is found, raise an HTTP exception
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not available")
    # If the blog exists, proceed to update it
    blog.update(request)
    db.commit()       # Committing the transaction (saving to the database)
    return 'updated good'








         #for getting data through id / single blog entry from the database by its id
       
@router.get('/{id}' , status_code = 200 , response_model=schemas.ShowBlog )
# The Function Receives the Path Parameter:
def show_data_by_id(id,  db: Session = Depends(get_db) ):
    blogs = db.query(models.Blog).filter(models.Blog.id == id).first()
    # logger.info(f"Retrieved blog: {blogs}")
    
   
    # creating custome status code according to need / conditions .
    if not blogs:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND , detail =f"Blog with the id {id} is not available" )
    #    response.status_code = status.HTTP_404_NOT_FOUND
    #    return {'detail' : f"Blog with the id {id} is not available "}
       
    return blogs
