"""SQL Alchemy database functions"""

from os import environ
from venv import logger

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from so_scrapper.scrappers.question import Question

_DB_NAME = environ.get("DB_NAME", "database.db")
_DB_URL = f"sqlite:///{_DB_NAME}"


def _create_db() -> Session:
    """Create the database"""
    engine = create_engine(_DB_URL)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.execute(
        "CREATE TABLE IF NOT EXISTS questions "
        + "(title TEXT, link TEXT, votes INTEGER, detail TEXT, tags TEXT, date TEXT)"
    )
    session.commit()
    logger.info("Database created")
    return session


def _add_question_to_db(session: Session, question: Question) -> None:
    """Add a question to the database"""
    session.execute(
        "INSERT INTO questions (title, link, "
        + "votes, detail, tags, date) VALUES (?, ?, ?, ?, ?, ?)",
        (
            question.title,
            question.link,
            question.votes,
            question.detail,
            question.tags,
            question.date,
        ),
    )
    session.commit()
    logger.info("Question added to the database")


def add_questions_to_db(questions: list[Question]) -> None:
    """Add questions to the database"""
    session = _create_db()
    for question in questions:
        _add_question_to_db(session, question)
    print("Questions added to the database")
    session.close()
