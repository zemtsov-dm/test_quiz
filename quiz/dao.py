from collections import deque
from datetime import datetime

from sqlalchemy import insert, select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from quiz.models import Question

from .tools import get_random_question


class QuestionsDAO:
    @classmethod
    async def get_question(
        cls,
        session: AsyncSession,
        question_id: int,
    ):
        stmt = select(Question).filter_by(id=question_id)
        result: Result = await session.execute(stmt)
        return result.scalars().all()

    @classmethod
    async def exists(
        cls,
        id: int,
        session: AsyncSession,
    ):
        stmt = select(Question).filter(Question.id == id)
        result: Result = await session.execute(stmt)
        # Проверяем, существует ли вопрос с указанным ID
        return result.scalar() is not None

    @classmethod
    async def get_last(
        cls,
        session: AsyncSession,
    ):
        stmt = select(Question).order_by(Question.save_date.desc()).offset(1).limit(1)
        result: Result = await session.execute(stmt)
        return result.scalar()

    @classmethod
    async def add_one(
        cls,
        question_data,
        session: AsyncSession,
    ):
        date_string = question_data["created_at"]
        date_format = "%Y-%m-%dT%H:%M:%S.%fZ"
        parsed_date = datetime.strptime(date_string, date_format)
        stmt = insert(Question).values(
            id=question_data["id"],
            question_text=question_data["question"],
            answer_text=question_data["answer"],
            create_date=parsed_date,
        )
        await session.execute(stmt)
        await session.commit()

    @classmethod
    async def add_many(
        cls,
        data,
        session: AsyncSession,
    ):
        question_stack = deque()
        for question in data:
            question_stack.append(question)
        while question_stack:
            question = question_stack.pop()
            print(question)
            if await cls.exists(question["id"], session=session):
                question_stack.append(await get_random_question())
            else:
                await cls.add_one(question, session=session)
