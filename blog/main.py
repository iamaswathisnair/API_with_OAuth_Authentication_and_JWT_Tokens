from fastapi import FastAPI , Depends , status , Response , HTTPException
from . import schemas , models
from .database import engine , SessionLocal
from sqlalchemy.orm import Session
from typing import List
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


app = FastAPI()


models.Base.metadata.create_all(engine)


def get_db(): #4
    db= SessionLocal()  # Creates a new session (connection) with the database
    try:
        yield db        # Provides this session for use in the request
    finally:
        db.close()      # Closes the session when done
       
       
       
       


                            # creation / for storing data
@app.post('/blog' , status_code = status.HTTP_201_CREATED)
def create(request : schemas.Blog, db: Session = Depends(get_db)): 
    new_blog = models.Blog(title=request.Title, body=request.Body) 
    db.add(new_blog)  # Using the session to add the new blog
    db.commit()       # Committing the transaction (saving to the database)
    db.refresh(new_blog)  # Refreshes the instance with the latest data from the database
    return new_blog










                                    #deletion
@app.delete('/blog/{id}' , status_code= status.HTTP_204_NO_CONTENT)
def delete(id , db: Session = Depends(get_db)):
   
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not available")
    # If the blog exists, proceed to update it
    blog.delete(synchronize_session = False)
    db.commit()       # Committing the transaction (saving to the database)
    # return 'Done'
   






                                    #updation
@app.put('/blog/{id}', status_code= status.HTTP_202_ACCEPTED)
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









                # Read / for getting all data/to fetch all blog entries from the database
@app.get('/blog', response_model= List[schemas.ShowBlog])
def show_all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs








               #for getting data through id / single blog entry from the database by its id
               
@app.get('/blog/{id}' , status_code = 200 , response_model=schemas.ShowBlog)
# The Function Receives the Path Parameter:
def show_data_by_id(id, response : Response, db: Session = Depends(get_db) ):
    blogs = db.query(models.Blog).filter(models.Blog.id == id).first()
    logger.info(f"Retrieved blog: {blogs}")
    
   
    # creating custome status code according to need / conditions .
    if not blogs:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND , detail =f"Blog with the id {id} is not available" )
    #    response.status_code = status.HTTP_404_NOT_FOUND
    #    return {'detail' : f"Blog with the id {id} is not available "}
       
    return blogs
   






@app.post('/user')
def create_user(request : schemas.User , db: Session = Depends(get_db)):
    new_user = models.User_model(Name=request.Name, Email=request.Email , Password=request.Password) 
    db.add(new_user)  
    db.commit()      
    db.refresh(new_user)  
    return new_user

    
  















