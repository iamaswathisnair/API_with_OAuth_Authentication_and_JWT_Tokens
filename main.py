from typing import Union , Optional
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI() #This creates an instance of the FastAPI app. app name change eeyam 
                #This app will listen for HTTP requests (like when someone visits a URL) and respond based on the code you write.

@app.get('/')   #in bracket its the url path (Root Endpoint (/) )and @app path operation decorator 
def index():
    return {'message': 'blog post'} 

#defining type for parameter
@app.get('/blog_type/{id}')
def show_type(id : int):
    return {'data':id} 

"""
Endpoint to retrieve blog data by ID.

Args:
    id (int): The unique identifier of the blog post.

Returns:
    dict: A dictionary containing the blog post ID.
"""

#id all are same if its blogid the 3 id will need to have blogid , {id} path parameter
@app.get('/blog/{id}')
def show(id):
    return {'data':id} 


@app.get('/blog/{id}/comments')
def comments(id):
    return {'data': f'comment with {id}'}
    # return {'data': 'comment with ' + str(id)}



#Query parameters to only get specific no.of data only
# http://127.0.0.1:8000/book?limit=10
@app.get('/book') 
def limit_show(limit):
    return {'message': f'{limit} books records from the database'} 



# http://127.0.0.1:8000/book?limit=10&published=true
# http://127.0.0.1:8000/book?limit=10&published=false

@app.get('/pens') 
def limit_show_pen(limit,published:bool):  #published should be a boolean this is an query parameter(True or False).
# def limit_show_pen(limit =10,published:bool = True): another eg 

       
        if published:
            return {'message': f'{limit} published books records from the database'}
        else:
            return {'message': f'{limit} unpublished books records from the database'}
        
class Blog(BaseModel):
      title : str
      body : str
      published : Optional[bool] = None

@app.post('/')       
def create(request:Blog):  #'BLOG' classil the model blog thane
    # return request
    return{'data': f"blog is created with title as : {request.title}"}
        