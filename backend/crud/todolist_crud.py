from sqlalchemy.orm import Session

from schemas.todolist_schemas import Todolist as Todolist_schemas
from models.todolist_models import TodoList as Todolist_models

def create_todolist_c(session:Session,list:Todolist_schemas):

    db_create = Todolist_models(notes=list.notes)

    session.add(db_create)
    session.commit(db_create)
    session.refresh(db_create)