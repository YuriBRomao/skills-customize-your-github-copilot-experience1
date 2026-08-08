"""Starter code for Python Text Processing assignment."""


def clean_text(text: str) -> str:
    """Return a normalized version of text.

    Steps expected in this assignment:
    1. Lowercase all letters
    2. Remove basic punctuation . , ! ? ; :
    3. Collapse repeated spaces
    """
    # TODO: implement
    pass


def count_words(file_path: str) -> dict:
    """Read a text file and return a frequency dictionary.

    Expected format:
    {
        "word": 3,
        "another": 1,
    }
    """
    # TODO: implement
    pass


def save_report(word_counts: dict, output_path: str) -> None:
    """Write sorted word frequencies to output_path.

    One entry per line in this format:
    word: frequency
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    # Optional manual test path.
    # Create a file like input.txt and run this script to test your functions.
    input_file = "input.txt"
    output_file = "report.txt"

    # Example flow (uncomment after implementing):
    # counts = count_words(input_file)
    # save_report(counts, output_file)
    pass
