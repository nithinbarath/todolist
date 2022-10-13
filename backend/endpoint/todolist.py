from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session

from schemas.todolist import CreateTodolist
from crud.todolist import create_list, get_todolist
from application import get_db_session

router = APIRouter()


@router.post("/create/todolist",tags=["todolist"])
def create_todolist(list:CreateTodolist, sessipn: Session = Depends(get_db_session)):

    return create_list(session=sessipn,list=list)

@router.get("/list/todolist" ,tags=['todolist'])
def list_todolist(session: Session = Depends(get_db_session)):

    return get_todolist(session=session)
