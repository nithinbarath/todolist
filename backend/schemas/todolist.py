from pydantic import BaseModel


class CreateTodolist(BaseModel):
    notes: str
    
