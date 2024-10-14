
# Defining What Data Looks Like for Users

# PYDANTIC MODEL 
from typing import List
from pydantic import BaseModel


# Schema for validating incoming data
class BlogBase(BaseModel):
    Title : str         #This class is for the user-facing side
    Body  : str
 
   
class Blog(BlogBase):
    class Config():
        from_attributes = True 
        
          
# User Schema for general user details           
class User(BaseModel):
    Name : str         #This class is for the user-facing side
    Email  : str
    Password  : str



class ShowUser(BaseModel):
    
    Name : str         #This class is for the user-facing side
    Email  : str
    blogs : List[Blog] = []
    
   
   
        
class ShowBlog(BaseModel):
    Title : str         #This class is for the user-facing side
    Body  : str
    userr : ShowUser
    
    class Config():
        from_attributes = True  # Correct for Pydantic v2.x
        orm_mode = True  # Use this to work with ORM objects
        
     
# Login Schema for authentication   
class Login(BaseModel):
    username: str
    password:str    