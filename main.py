from typing import Union

from fastapi import FastAPI

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

#id all are same if its blogid the 3 id will need to have blogid
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
