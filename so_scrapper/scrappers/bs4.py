"""Stackoverflow scrapper module using BeautifulSoup and requests."""

from datetime import datetime

from bs4 import BeautifulSoup
from loguru import logger
from requests import get

from so_scrapper.scrappers.question import Question

_BASE_URL = "https://stackoverflow.com/questions/"


def _find_votes(soup: BeautifulSoup) -> int | None:
    """Find votes in Stack Overflow question"""
    try:
        vote_count_div = soup.find(
            "div", class_="js-vote-count", itemprop="upvoteCount"
        )
        vote_count = int(vote_count_div["data-value"])
        return vote_count
    except (Exception, TypeError, ValueError) as e:
        logger.exception(e)


def _find_question_text(soup: BeautifulSoup) -> str | None:
    """Find question text in Stack Overflow question"""
    try:
        question_div = soup.find("div", class_="question")
        return question_div.find("div", class_="s-prose js-post-body").get_text()
    except Exception as e:
        logger.exception(e)
        return None


def _find_tags(soup: BeautifulSoup) -> list[str] | None:
    """Find tags in Stack Overflow question"""
    try:
        tags_div = soup.find("div", class_="post-taglist")
        return [tag.get_text(strip=True) for tag in tags_div.find_all("a")]
    except Exception as e:
        logger.exception(e)
        return None


def _find_title_url(soup: BeautifulSoup) -> str | None:
    """Find title link in Stack Overflow question"""
    try:
        title_link = soup.select_one("#question-header > h1 > a")
        if title_link is not None:
            return title_link.get("href")
    except Exception as e:
        logger.exception(e)
        return None


def _find_creation_date(soup: BeautifulSoup) -> datetime | None:
    """Find creation date in Stack Overflow question"""
    try:
        creation_date = (
            soup.find("time", itemprop="dateCreated")["datetime"]
            .replace("T", " ")
            .replace("Z", "")
        )
        return datetime.strptime(creation_date, "%Y-%m-%d %H:%M:%S")
    except Exception as e:
        logger.exception(e)
        return None


def _find_url(title_link: str | None) -> str | None:
    """Find URL in Stack Overflow question"""
    if title_link is None:
        return None
    try:
        return _BASE_URL + title_link
    except Exception as e:
        logger.exception(e)
        return None


def _find_title(title_link: str | None) -> str | None:
    """Find title in Stack Overflow question"""
    if title_link is None:
        return None
    try:
        return title_link.split("/")[-1]
    except Exception as e:
        logger.exception(e)
        return None


def get_question_w_bs4(id: int) -> Question:
    """Get Stack Overflow question by ID"""
    response = get(f"{_BASE_URL}{id}")
    soup = BeautifulSoup(response.content, "html.parser")
    votes = _find_votes(soup)
    title_link = _find_title_url(soup)
    title = _find_title(title_link)
    detail = _find_question_text(soup)
    tags = _find_tags(soup)
    date = _find_creation_date(soup)
    url = _find_url(title_link)
    return Question(
        title=title, link=url, votes=votes, detail=detail, tags=tags, date=date
    )
