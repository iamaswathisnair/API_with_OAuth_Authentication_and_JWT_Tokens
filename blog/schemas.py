# Defining What Data Looks Like for Users

# PYDANTIC MODEL 

from pydantic import BaseModel


# Schema for validating incoming data
class Blog(BaseModel):
    Title : str         #This class is for the user-facing side
    Body  : str
    
class ShowBlog(Blog):
    class Config():
        from_attributes = True  # Correct for Pydantic v2.x
        orm_mode = True  # Use this to work with ORM objects
          
    
class User(BaseModel):
    Name : str         #This class is for the user-facing side
    Email  : str
    Password  : str
    