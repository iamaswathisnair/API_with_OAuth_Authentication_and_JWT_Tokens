#Defining What Data Looks Like for Users

from pydantic import BaseModel

class Blog(BaseModel):
    Title : str     #This class is for the user-facing side
    Body  : str
    