from typing import Union
from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from schemas.todolist_schemas import Todolist
# from crud.todolist_crud import create_todolist_c
# from application import get_db_session
# from crud.todolist_crud import create_todolist_c
from backend.crud.todolist_crud import create_todolist_c

router = APIRouter()


@router.get("/",tags=['verify'])
def read_root():
    return {"Hello": "World"}


@router.get("/items/{item_id}",tags=['verify'])
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


# @router.post("/create",tags=['verify'])
# def create_todolist(list:Todolist,db: Session = Depends(get_db_session)):
    
#     db_todolist = 1
#     if db_todolist:
#         raise HTTPException(status_code=400, detail="list already exists")

#     return crud_todo(session=db,list=list)

# @router.post("/users/",tags=["Users"])
# def create_user(user: Todolist, db: Session = Depends(get_db_session)):
#     db_user = 1
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return  HTTPException(status_code=400, detail="list already exists")