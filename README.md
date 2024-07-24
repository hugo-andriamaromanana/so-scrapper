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
python console_scripts/scrapper.py [OPTIONS]
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

This command scrapes Stack Overflow using BeautifulSoup, making 10 requests, and saves the results in `results.csv` using the CSV format.

### Strategy Pattern

The project utilizes the strategy pattern for both scraping and saving data. This allows for easy extension and integration of different scraping and saving methods without modifying the core logic.

- **Scraping Strategy**: Implemented in [`so_scrapper/scrappers/`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Ffo%2FEkol%2Fso-scrapper%2Fso_scrapper%2Fscrappers%2F%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "/home/fo/Ekol/so-scrapper/so_scrapper/scrappers/"). Each scraping method (e.g., `bs4.py`) defines a strategy for extracting data from Stack Overflow.
- **Saving Strategy**: Implemented in [`so_scrapper/saves/`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Ffo%2FEkol%2Fso-scrapper%2Fso_scrapper%2Fsaves%2F%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "/home/fo/Ekol/so-scrapper/so_scrapper/saves/"). Each save method (e.g., `csv.py`) defines a strategy for persisting the scraped data.

### Error Handling

[`so-scrapper`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2Fhome%2Ffo%2FEkol%2Fso-scrapper%2FREADME.md%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A0%2C%22character%22%3A0%7D%5D "README.md") includes basic error handling to manage common issues such as network errors, invalid arguments, and scraping errors. It ensures the program exits gracefully, providing meaningful error messages to the user.

## Contributing

Contributions to [`so-scrapper`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2Fhome%2Ffo%2FEkol%2Fso-scrapper%2FREADME.md%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A0%2C%22character%22%3A0%7D%5D "README.md") are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Commit your changes with meaningful messages.
4. Push your branch and submit a pull request.

Please ensure your code adheres to the project's coding standards and includes appropriate tests.

## License

Specify your project's license here.

```

This template provides a solid foundation for your project's README. You can customize it further based on your project's specific requirements and features.