from fastapi import FastAPI 
from blog import  models
from blog.database import engine 
from blog.routers import  blog_router , user_router , authentication


import os
print(os.getcwd())  # Prints current working directory to help with debugging


app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "Welcome to my FastAPI application!"}


models.Base.metadata.create_all(engine)

# Include the blog router and user router
app.include_router(authentication.router) 
app.include_router(blog_router.router)  # The 'prefix' is optional but adds clarity to the URL
app.include_router(user_router.router)
 
# Now all blog/user routes will be available under the /api path.


# This block ensures that the FastAPI app runs when this file is executed directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
