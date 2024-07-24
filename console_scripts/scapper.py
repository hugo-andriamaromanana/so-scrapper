"""Main module to add questions to the database"""

from so_scrapper.arg_parser import parse_args
from so_scrapper.saves.save import SaveMethod, save_questions
from so_scrapper.scrappers.scrapper import ScrapType, get_questions


def main() -> None:
    """Main function"""
    params = parse_args()
    questions = get_questions(ScrapType[params.scrap_method], params.nb_of_requests)
    save_questions(
        questions,
        SaveMethod[params.save_method],
    )


if __name__ == "__main__":
    main()
