# Defining How Data is Stored in the Database
#SQLALCHEMY MODEL 

from sqlalchemy import Column ,Integer , String 
from .database import Base

class Blog(Base):
    
    __tablename__ = 'blog'  #tells SQLAlchemy to create a table called blog.
    
    id = Column(Integer,primary_key=True,index=True)
    Title = Column(String)
    Body =  Column(String)
    

class User_model(Base):
    
    __tablename__ = 'Users'  #tells SQLAlchemy to create a table called Users.
    
    id = Column(Integer,primary_key=True,index=True)
    Name = Column(String)
    Email =  Column(String)
    Password =  Column(String)

    