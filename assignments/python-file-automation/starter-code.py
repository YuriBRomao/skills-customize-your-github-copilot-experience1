"""Starter code for Python File Automation assignment."""

from __future__ import annotations

import csv
from pathlib import Path


def load_files(file_path: str) -> list[dict]:
    """Read a CSV file and return a list of file records.

    Expected CSV columns:
    - name
    - type
    - size_kb
    """
    # TODO: implement
    pass


def build_summary(files: list[dict]) -> dict:
    """Build a summary from loaded file records."""
    # TODO: implement
    pass


def save_report(summary: dict, output_path: str) -> None:
    """Write a readable text report to output_path."""
    # TODO: implement
    pass


if __name__ == "__main__":
    sample_input = Path("data.csv")
    sample_output = Path("report.txt")

    # Example flow (uncomment after implementing):
    # files = load_files(str(sample_input))
    # summary = build_summary(files)
    # save_report(summary, str(sample_output))
    pass
