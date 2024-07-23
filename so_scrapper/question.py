"""Model for Stack Overflow Question"""

from datetime import datetime
from pydantic import BaseModel

class Question(BaseModel):
    """Stack Overflow Question Model"""
    title: str
    link: str
    votes: int
    detail: str
    tags: list[str]
    date: datetime
