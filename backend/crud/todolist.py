from sqlalchemy.orm import Session
from schemas import question as schema_question
from models import question as model_question
from models import question
from schemas.todolist import CreateTodolist
from models.todolist import Todolist

def get_by_question(db: Session,question: str):

    return db.query(model_question.Question).filter(model_question.Question.question== question).first()

def create_question(db: Session, questions: schema_question.CreateQuestions):
    db_question = model_question.Question(question=questions.question,optionA = questions.optionA,optionB = questions.optionB,optionC = questions.optionC,optionD = questions.optionD)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question



def create_list(session: Session, note:CreateTodolist):
    
    db_todolist = Todolist(notes=note.notes)
    session.add(db_todolist)
    session.commit()
    session.refresh(db_todolist)
    return db_todolist