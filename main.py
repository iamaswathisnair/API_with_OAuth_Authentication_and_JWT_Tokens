from typing import Union

from fastapi import FastAPI

app = FastAPI() #This creates an instance of the FastAPI app.
                #This app will listen for HTTP requests (like when someone visits a URL) and respond based on the code you write.

def index():
    return "HEY ASWATHiii"    
