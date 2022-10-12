from starlette.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware
from fastapi import FastAPI
from os import environ
import uvicorn

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

from endpoints.verify.testing import router as verify_router



def get_db_session():
    db: Session = db_session()
    try:
        yield db
    finally:
        db.close()


DATABASE_URL = environ['DB_URI']
print(DATABASE_URL)
Base = declarative_base()
db_engine = create_engine(
    DATABASE_URL, connect_args={'connect_timeout': 10},
    pool_size=100, echo=False
)
db_session = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)


origins = [
        "http://localhost:8080/"
    ]

middleware = [
        Middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=['*'],
            allow_headers=['*']
        )
    ]


app = FastAPI(middleware=middleware)


app.include_router(verify_router, prefix="/api/v1")
# app.include_router(todolist_router, prefix="/api/v1")


if __name__ == '__main__':
    uvicorn.run(app, port=9559, host="0.0.0.0")

