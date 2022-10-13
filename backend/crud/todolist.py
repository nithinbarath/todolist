from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.todolist import Todolist
from schemas.todolist import CreateTodolist



def create_list(session: Session, list:CreateTodolist):

    record = session.query(Todolist).filter(Todolist.notes == list.notes).first()

    if record:
        raise HTTPException(status_code=400, detail="Notes Already Created")
    else:
        db_todolist = Todolist(notes=list.notes)
        session.add(db_todolist)
        session.commit()
        session.refresh(db_todolist)
        return db_todolist

def get_todolist(session: Session):

    record = session.query(Todolist).all()

    return record