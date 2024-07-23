"""Stackoverflow scrapper module using BeautifulSoup and requests."""

from requests import get
from bs4 import BeautifulSoup
from datetime import datetime
from so_scrapper.question import Question

_BASE_URL = "https://stackoverflow.com/questions/"

def _find_votes(soup: BeautifulSoup) -> int:
    """Find votes in Stack Overflow question"""
    vote_count_div = soup.find("div", class_="js-vote-count", itemprop="upvoteCount")
    return int(vote_count_div['data-value'])

def _find_question_text(soup: BeautifulSoup) -> str:
    """Find question text in Stack Overflow question"""
    question_div = soup.find("div", class_="question")
    return question_div.find("div", class_="s-prose js-post-body").get_text()

def _find_tags(soup: BeautifulSoup) -> list[str]:
    """Find tags in Stack Overflow question"""
    tags_div = soup.find("div", class_="post-taglist")
    return [tag.get_text(strip=True) for tag in tags_div.find_all("a")]

def _find_title_url(soup: BeautifulSoup) -> str:
    """Find title link in Stack Overflow question"""
    title_link = soup.select_one("#question-header > h1 > a")['href']
    return title_link

def _find_creation_date(soup: BeautifulSoup) -> datetime:
    """Find creation date in Stack Overflow question"""
    creation_date = soup.find("time", itemprop="dateCreated")['datetime'].replace("T", " ").replace("Z", "")
    return datetime.strptime(creation_date, "%Y-%m-%d %H:%M:%S")

def _find_url(title_link: str) -> str:
    """Find URL in Stack Overflow question"""
    return _BASE_URL + title_link

def _find_title(title_link: str) -> str:
    """Find title in Stack Overflow question"""
    return title_link.split("/")[-1]

def get_question(id: int) -> Question:
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
    return Question(title=title, link=url, votes=votes, detail=detail, tags=tags, date=date)