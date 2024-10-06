from fastapi import FastAPI , Depends #3
from . import schemas , models 
from .database import engine , SessionLocal #5
from sqlalchemy.orm import Session #2

app = FastAPI() 

models.Base.metadata.create_all(engine)

def get_db(): #4
    db= SessionLocal()  # Creates a new session (connection) with the database
    try:
        yield db        # Provides this session for use in the request
    finally:
        db.close()      # Closes the session when done

#for storing data
@app.post('/blog')
def create(request : schemas.Blog, db: Session = Depends(get_db)): #1
    new_blog = models.Blog(title=request.Title, body=request.Body) #6
    db.add(new_blog)  # Using the session to add the new blog
    db.commit()       # Committing the transaction (saving to the database)
    db.refresh(new_blog)  # Refreshes the instance with the latest data from the database
    return new_blog


#for getting all data
@app.get('/blog')
def show_all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


#for getting data through id
@app.get('/blog/{id}')
def show_data_by_id(id, db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).filter(models.Blog.id == id).first
    return blogs

