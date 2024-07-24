"""Command line arguments parser"""

from argparse import ArgumentParser
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Params:
    """Command line arguments"""

    output_path: Path
    nb_of_requests: int
    scrap_method: str
    save_method: str


def parse_args() -> Params:
    """Parse command line arguments"""
    parser = ArgumentParser(description="Scrap Stack Overflow")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default="output.csv",
        help="Output file path",
    )
    parser.add_argument(
        "-n",
        "--number",
        type=int,
        default=1,
        help="Number of requests",
    )
    parser.add_argument(
        "-m",
        "--method",
        type=str,
        default="BS4",
        help="Scraping method",
    )
    parser.add_argument(
        "-s",
        "--save",
        type=str,
        default="CSV",
        help="Save method",
    )
    args = parser.parse_args()
    return Params(
        output_path=args.output,
        nb_of_requests=args.number,
        scrap_method=args.method,
        save_method=args.save,
    )
