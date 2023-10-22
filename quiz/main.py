from datetime import datetime

from fastapi import Depends, FastAPI
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from quiz.dao import QuestionsDAO
from quiz.database import get_session

from quiz.tools import get_random_questions

app = FastAPI()


class Question(BaseModel):

    id: int
    question_text:str
    answer_text: str
    create_date: datetime


@app.post("/", response_model=Question)
async def get_quiz_questions(
    questions_number: int,
    session: AsyncSession = Depends(get_session),
):
    questions = await get_random_questions(questions_number)
    await QuestionsDAO.add_many(questions, session)
    return await QuestionsDAO.get_last(session)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
