from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from quiz.database import Base


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    question_text = Column(String, index=True)
    answer_text = Column(String)
    create_date = Column(DateTime, default=datetime.utcnow)
    save_date = Column(DateTime, default=datetime.utcnow)
