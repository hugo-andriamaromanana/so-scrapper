"""Module to save questions to a file or a database"""

from enum import Enum, auto
from multiprocessing.pool import ThreadPool as Pool
from pathlib import Path
from sys import exit as sys_exit

from loguru import logger

from so_scrapper.saves.mongo import add_questions_to_mongo
from so_scrapper.saves.ptdf import ptdf
from so_scrapper.saves.sql_alchemy import add_questions_to_db
from so_scrapper.scrappers.question import Question

OUTPUT_PATH = Path("questions.csv")


def add_questions_to_sql_parallel(questions: list[Question]) -> None:
    """Add questions to the database in parallel"""
    pool = Pool()
    pool.map(add_questions_to_db, [questions])
    pool.close()
    pool.join()
    logger.info("Questions added to the database in parallel")


def add_questions_to_csv(questions: list[Question]) -> None:
    """Add questions to a CSV file"""
    df_questions = ptdf(questions)
    df_questions.to_csv(OUTPUT_PATH, index=False)


class SaveMethod(str, Enum):
    """Enum for saving methods"""

    CSV = auto()
    DB = auto()
    MONGO = auto()


_SAVING_MAP = {
    SaveMethod.CSV: add_questions_to_csv,
    SaveMethod.DB: add_questions_to_sql_parallel,
    SaveMethod.MONGO: add_questions_to_mongo
}


def save_questions(questions: list[Question], save_method: SaveMethod) -> None:
    """Save questions to a file or a database"""
    try:
        _SAVING_MAP[save_method](questions)
    except KeyError as e:
        logger.critical(f"Method Not Implemented, couldn't save:\n{e}")
        sys_exit(1)
    except Exception as e:
        logger.error(f"Couldn't save:\n{e}")
        sys_exit(1)
    logger.info("Questions saved")
