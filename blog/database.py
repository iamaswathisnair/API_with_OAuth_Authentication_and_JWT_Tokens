from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



#Define the Database URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"


# Create the engine (connection to database)
engine = create_engine(SQLALCHEMY_DATABASE_URL , connect_args ={"check_same_thread" : False} )

SessionLocal = sessionmaker(bind = engine , autocommit=False , autoflush=False)

Base = declarative_base()
