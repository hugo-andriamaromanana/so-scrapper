"""Bridge and error management for scrappers"""

from enum import Enum, auto
from http.client import HTTPException
from random import randint
from sys import exit as sys_exit
from typing import Callable

from loguru import logger

from so_scrapper.scrappers.api import get_question_w_api
from so_scrapper.scrappers.bs4 import get_question_w_bs4
from so_scrapper.scrappers.question import Question


class ScrappingType(str, Enum):
    """Enum for scrapper types"""

    API = auto()
    BS4 = auto()


_ScrappingFunc = Callable[[int], Question]

_SCRAPPERS_MAP: dict[ScrappingType, _ScrappingFunc] = {
    ScrappingType.API: get_question_w_api,
    ScrappingType.BS4: get_question_w_bs4,
}


def get_questions(method: ScrappingType, nb_of_requests: int | float) -> list[Question]:
    """Uses the scapping method"""
    questions = []
    for _ in range(int(nb_of_requests)):
        try:
            questions.append(_SCRAPPERS_MAP[method](randint(0,20000000)))
        except HTTPException as e:
            logger.warning(f"HTTP Error, no network or server:\n{e}")
        except KeyError as e:
            logger.critical(f"Method Not Implemented, couldn't fetch:\n{e}")
            sys_exit(1)
    return questions