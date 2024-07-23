from enum import Enum, auto
from typing import Callable

from so_scrapper.scrappers.question import Question
from so_scrapper.scrappers.api import get_question_w_api
from so_scrapper.scrappers.bs4 import get_question_w_bs4


class ScrappingType(str, Enum):
    """Enum for scrapper types"""

    API = auto()
    BS4 = auto()


_ScrappingFunc = Callable[[int], Question]

_SCRAPPERS_MAP: dict[ScrappingType, _ScrappingFunc] = {
    ScrappingType.API: get_question_w_api,
    ScrappingType.BS4: get_question_w_bs4,
}
