"""Main module of the so_scrapper package"""
from venv import logger
from so_scrapper.scrappers.question import Question
from so_scrapper.scrappers.scrapper import ScrappingType, get_questions
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from os import environ

_DB_NAME = environ.get("DB_NAME", "database.db")
_DB_URL = f"sqlite:///{_DB_NAME}"


def create_db() -> Session:
    """Create the database"""
    engine = create_engine(_DB_URL)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.execute(
        "CREATE TABLE IF NOT EXISTS questions (title TEXT, link TEXT, votes INTEGER, detail TEXT, tags TEXT, date TEXT)"
    )
    session.commit()
    logger.info("Database created")
    return session


def add_question_to_db(session: Session, question: Question) -> None:
    """Add a question to the database"""
    session.execute(
        "INSERT INTO questions (title, link, votes, detail, tags, date) VALUES (?, ?, ?, ?, ?, ?)",
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


def add_questions_to_db(method: ScrappingType, nb_of_requests: int) -> None:
    """Add questions to the database"""
    session = create_db()
    questions = get_questions(method, nb_of_requests)
    for question in questions:
        add_question_to_db(question)
    print("Questions added to the database")
    session.close()