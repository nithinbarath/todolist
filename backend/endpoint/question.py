from typing import List
from fastapi import FastAPI , Depends,HTTPException,status
from sqlalchemy.orm import Session
from fastapi import APIRouter
from crud import question as crud_question
from schemas import question as schema_question
from models import question as model_question
from application import get_db_session

router = APIRouter()


@router.get("/questions/", response_model=List[schema_question.ShowQuestions],tags=["Admin Questions"])
def get_question(skip: int = 0, limit: int = 100, db: Session = Depends(get_db_session)):
    users = crud_question.get_users(db,skip=skip, limit=limit)
    return users

@router.post("/questions/", response_model=schema_question.ShowQuestions,tags=["Admin Questions"])
def create_question(create_question: schema_question.CreateQuestions, db: Session = Depends(get_db_session)):
    db_user = crud_question.get_by_question(db,question=create_question.question)
    if db_user:
        raise HTTPException(status_code=400, detail="Question Already Created")
    return crud_question.create_question(db=db,questions=create_question)

@router.delete("/questions/{questions_id}/", tags=["Admin Questions"])
def delete_question(job_id:int,db: Session = Depends(get_db_session)):
   db_delete = crud_question.question_delete(db, job_id=job_id)

   return db_delete

@router.put("/questions/{question_id}",response_model=schema_question.QuestionUpdate,tags=["Admin Questions"])
def update_question(question:schema_question.QuestionUpdate,question_id=int,  db: Session = Depends(get_db_session)):

    return crud_question.question_update(db=db,question_id=question_id,question=question)
