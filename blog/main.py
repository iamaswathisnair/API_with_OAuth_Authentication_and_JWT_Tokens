from fastapi import FastAPI 
from . import  models
from .database import engine 
from . routers import  blog_router , user_router , authentication


app = FastAPI()


models.Base.metadata.create_all(engine)

# Include the blog router and user router
app.include_router(authentication.router) 
app.include_router(blog_router.router)  # The 'prefix' is optional but adds clarity to the URL
app.include_router(user_router.router)
 
# Now all blog/user routes will be available under the /api path.



       
       
       
       


              






                                    
   





                           