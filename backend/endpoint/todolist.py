from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session

from schemas.todolist import CreateTodolist
from crud.todolist import create_list
from application import get_db_session

router = APIRouter()


@router.post("/todolist",tags=["todolist"])
def create_todolist(list:CreateTodolist, sessipn: Session = Depends(get_db_session)):

    return create_list(session=sessipn,note=list)
    
