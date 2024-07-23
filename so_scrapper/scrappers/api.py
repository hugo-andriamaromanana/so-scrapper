"""Stackoverflow scrapper module using Stack Overflow API."""

from datetime import datetime
from os import environ

from requests import get as requests_get

from so_scrapper.scrappers.question import Question

_BASE_URL = "https://api.stackexchange.com/2.3/questions/"
_API_KEY = environ.get("STACK_OVERFLOW_API_KEY")


def _find_votes(data: dict) -> int | None:
    """Find votes in Stack Overflow question"""
    return data.get("score")


def _find_question_text(data: dict) -> str | None:
    """Find question text in Stack Overflow question"""
    return data.get("body")


def _find_tags(data: dict) -> list[str] | None:
    """Find tags in Stack Overflow question"""
    return data.get("tags", [])


def _find_creation_date(data: dict) -> datetime | None:
    """Find creation date in Stack Overflow question"""
    date = data.get("creation_date")
    if date is None:
        return None
    return datetime.fromtimestamp(date)


def _find_url(data: dict) -> str | None:
    """Find URL in Stack Overflow question"""
    return data.get("link")


def _find_title(data: dict) -> str | None:
    """Find title in Stack Overflow question"""
    return data.get("title")


def get_question_w_api(id: int) -> Question:
    """Get Stack Overflow question by ID"""
    params = {"site": "stackoverflow", "filter": "withbody", "key": _API_KEY}
    response = requests_get(f"{_BASE_URL}{id}", params=params)
    data = response.json()["items"][0]
    votes = _find_votes(data)
    title = _find_title(data)
    detail = _find_question_text(data)
    tags = _find_tags(data)
    date = _find_creation_date(data)
    url = _find_url(data)
    return Question(
        title=title, link=url, votes=votes, detail=detail, tags=tags, date=date
    )
