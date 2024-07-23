"""Model for Stack Overflow Question"""

from datetime import datetime

from pydantic import BaseModel


class Question(BaseModel):
    """Stack Overflow Question Model"""

    title: str | None
    link: str | None
    votes: int | None
    detail: str | None
    tags: list[str] | None
    date: datetime | None

    @property
    def is_negative(self) -> bool:
        """Check if the question has negative votes"""
        return self.votes is not None and self.votes < 0
