from pydantic import BaseModel

class Blog(BaseModel):
    Title : str
    Body  : str
    