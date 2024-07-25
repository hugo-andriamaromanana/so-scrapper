"""Testing Module for scrappers.py"""

from unittest import TestCase
from unittest.mock import patch

from so_scrapper.scrappers.scrapper import ScrapType, get_questions


class TestScrapper(TestCase):
    """Test the scrapper module"""

    @patch("so_scrapper.scrappers.scrapper.get_question_w_api")
    def test_get_questions_api(self, mock_get_question_w_api):
        """Test get questions with API"""
        mock_get_question_w_api.return_value = None
        questions = get_questions(ScrapType.API, 1)
        self.assertEqual(questions, [])

    @patch("so_scrapper.scrappers.scrapper.get_question_w_bs4")
    def test_get_questions_bs4(self, mock_get_question_w_bs4):
        """Test get questions with BS4"""
        mock_get_question_w_bs4.return_value = None
        questions = get_questions(ScrapType.BS4, 1)
        self.assertEqual(questions, [])
