from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from schemas.todolist import CreateTodolist, UpdateTodolist, DeleteTodolist
from crud.todolist import create_list, get_todolist, update_todolist, delete_todolist
from application import get_db_session

router = APIRouter()


@router.post("/create/todolist",tags=["todolist"])
def create_todolist(list:CreateTodolist, sessipn: Session = Depends(get_db_session)):

    return create_list(session=sessipn,list=list)

@router.get("/list/todolist" ,tags=['todolist'])
def list_todolist(session: Session = Depends(get_db_session)):

    return get_todolist(session=session)

@router.put("/update/todolist",tags=['todolist'])
def update_list(list: UpdateTodolist, session: Session = Depends(get_db_session)):
    
    return update_todolist(session=session,list=list)

@router.delete('/delete/todolist',tags=['todolist'])
def delete_list(list:DeleteTodolist, session: Session = Depends(get_db_session)):

    return delete_todolist(session=session, list_id=list)
