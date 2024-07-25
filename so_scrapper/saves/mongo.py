"""MongoDB save module."""

from os import environ

from loguru import logger
from pymongo import MongoClient

from so_scrapper.scrappers.question import Question

MONGO_DB = environ.get("MONGO_DB", "stackoverflow")
MONGO_COLLECTION = environ.get("MONGO_COLLECTION", "questions")


def add_questions_to_mongo(questions: list[Question]) -> None:
    """Add questions to the MongoDB database"""
    mongo = MongoClient()
    db = mongo[MONGO_DB]
    collection = db[MONGO_COLLECTION]
    for question in questions:
        collection.insert_one(question.dict())
    logger.info("Questions added to MongoDB")
    mongo.close()
