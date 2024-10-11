# Defining How Data is Stored in the Database
#SQLALCHEMY MODEL 

from sqlalchemy import Column ,Integer , String  , ForeignKey
from .database import Base
from sqlalchemy.orm import relationship


# Blog Model (Each blog belongs to one user)
class Blog(Base):
    
    __tablename__ = 'blog'  #tells SQLAlchemy to create a table called blog.
    
    id = Column(Integer,primary_key=True,index=True)
    Title = Column(String)
    Body =  Column(String)
    
    # Foreign Key to link each blog to a user
    user_id = Column(Integer, ForeignKey('Users.id'))  # Reference to User_model.id
    
    # Relationship back to the User_model table
    userr = relationship("User_model", back_populates="blogs")  
    
    
# User Model (Each user can have many blogs)
class User_model(Base):
    
    __tablename__ = 'Users'  #tells SQLAlchemy to create a table called Users.
    
    id = Column(Integer,primary_key=True,index=True)
    Name = Column(String)
    Email =  Column(String)
    Password =  Column(String)
    
    # One user can have many blogs
    blogs = relationship("Blog", back_populates="userr")
