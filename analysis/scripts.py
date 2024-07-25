"""This module contains functions to analyze the Stack Overflow data"""

from ast import literal_eval
from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt
from pandas import read_csv

_STACK_DATA_PATH = Path("../data/questions.csv")
_STACK_DATA = read_csv(_STACK_DATA_PATH)


def count_votes_by_tag() -> dict[str, int]:
    """Count the number of votes per tag"""
    copy = _STACK_DATA.copy()
    copy["tags"] = copy["tags"].apply(literal_eval)
    tags = copy.explode("tags")
    votes_by_tag = (
        tags.groupby("tags")["votes"].sum().sort_values(ascending=False).to_dict()
    )
    return votes_by_tag


def plot_votes_by_tag():
    """Plot the number of votes per tag"""
    votes_by_tag = count_votes_by_tag()
    top_50_votes_by_tag = dict(list(votes_by_tag.items())[:50])
    plt.figure(figsize=(12, 6))
    plt.bar(top_50_votes_by_tag.keys(), top_50_votes_by_tag.values())
    plt.xlabel("Tags")
    plt.ylabel("Number of Votes")
    plt.title("Number of Votes per Tag")
    plt.xticks(rotation=55)
    plt.show()


def plot_questions_by_tag():
    """Plot the number of questions per tag"""
    questions_by_tag = count_questions_by_tag()
    top_50_questions_by_tag = dict(list(questions_by_tag.items())[:50])
    plt.figure(figsize=(12, 6))
    plt.bar(top_50_questions_by_tag.keys(), top_50_questions_by_tag.values())
    plt.xlabel("Tags")
    plt.ylabel("Number of Questions")
    plt.title("Number of Questions per Tag")
    plt.xticks(rotation=55)
    plt.show()


def count_questions_by_tag() -> dict[str, int]:
    """Count the number of questions per tag"""
    copy = _STACK_DATA.copy()
    copy["tags"] = copy["tags"].apply(literal_eval)
    tags = copy.explode("tags")
    questions_by_tag = (
        tags.groupby("tags").size().sort_values(ascending=False).to_dict()
    )
    return questions_by_tag


def plot_posts_by_month():
    """Plot the number of posts per month"""
    copy = _STACK_DATA.copy()
    copy["date"] = copy["date"].apply(
        lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S")
    )
    copy["month"] = copy["date"].dt.month_name()
    posts_by_month = copy.groupby("month").size()
    months_order = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    posts_by_month = posts_by_month.reindex(months_order)
    plt.figure(figsize=(12, 6))
    ax = posts_by_month.plot(kind="bar")
    ax.set_xticklabels(posts_by_month.index, rotation=55)
    plt.xlabel("Month")
    plt.ylabel("Number of Posts")
    plt.title("Number of Posts per Month")
    plt.show()
