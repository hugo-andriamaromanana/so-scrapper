# so-scrapper

`so-scrapper` is a Python-based command-line tool designed to scrape Stack Overflow. It allows users to specify the number of requests, the output file path, the scraping method, and the save method.

## Installation

```sh
git clone https://github.com/hugo-andriamaromanana/so-scrapper.git
cd so-scrapper
poetry build
pip install dist/so_scrapper-0.1.0-py3-none-any.whl
```

## Usage

To use [`so-scrapper`]("README.md"), run the [`scrapper.py`]("console_scripts/scrapper.py") script from the command line with the desired arguments:

```sh
so-scrapper [-h] [-o OUTPUT] [-n NUMBER] [-m METHOD] [-s SAVE]
```

### CLI Arguments

- `-o`, `--output`: Specify the output file path (default: `output.csv`).
- `-n`, `--number`: Specify the number of requests (default: 1).
- `-m`, `--method`: Specify the scraping method (`BS4` for BeautifulSoup, other methods may be available) (default: `BS4`).
- `-s`, `--save`: Specify the save method (`CSV` for saving as CSV, other methods may be available) (default: `CSV`).

Example:

```sh
python console_scripts/scrapper.py -o results.csv -n 10 -m BS4 -s CSV
```

This command scrapes Stack Overflow using BeautifulSoup, making 10 requests, and saves the results in `output.csv` using the CSV format.

### Strategy Pattern

The project utilizes the strategy pattern for both scraping and saving data. This allows for easy extension and integration of different scraping and saving methods without modifying the core logic.

- **Scraping Strategy**: Implemented in [`so_scrapper/scrappers/`]( "so_scrapper/scrappers/"). Each scraping method (e.g., `bs4.py`) defines a strategy for extracting data from Stack Overflow.
- **Saving Strategy**: Implemented in [`so_scrapper/saves/`]("so_scrapper/saves/"). Each save method (e.g., `csv.py`) defines a strategy for persisting the scraped data.

### Error Handling

[`so-scrapper`]("README.md") includes basic error handling to manage common issues such as network errors, invalid arguments, and scraping errors. It ensures the program exits gracefully, providing meaningful error messages to the user.

