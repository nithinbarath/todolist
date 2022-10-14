from fastapi.middleware.cors import CORSMiddleware
from fastapi import  FastAPI
import logging

from user import api_router


logger = logging.getLogger(__name__)


app = FastAPI(title="backend")

origins= [
    'http://localhost:8000',
    'http://localhost:8080',
    'http://127.0.0.1:8000',
    'http://127.0.0.1:8080'
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


app.include_router(api_router,prefix='/api')