# Defining How Data is Stored in the Database

from sqlalchemy import Column ,Integer , String 
from .database import Base

class Blog(Base):
    
    __tablename__ = 'blog'  #tells SQLAlchemy to create a table called blog.
    
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String)
    body =  Column(String)
    