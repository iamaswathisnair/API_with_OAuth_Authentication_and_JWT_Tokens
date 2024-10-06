from fastapi import FastAPI , Depends #3
from . import schemas , models 
from .database import engine , SessionLocal #5
from sqlalchemy.orm import Session #2

app = FastAPI() 

models.Base.metadata.create_all(engine)

def get_db(): #4
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/blog')
def create(request : schemas.Blog, db: Session = Depends(get_db)): #1
    new_blog = models.Blog(title=request.Title, body=request.Body) #6
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog