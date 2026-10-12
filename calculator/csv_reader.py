
"""Read numeric CSV columns using pandas."""

from pathlib import Path

import pandas as pd

from calculator.validation import numeric_values


def read_csv_numbers(path: str, column: str) -> tuple[float, ...]:
    """Load a CSV column and validate every value."""
    if not path or not column:
        raise ValueError("CSV path and column are required.")

    try:
        data = pd.read_csv(Path(path))
    except (OSError, pd.errors.ParserError, pd.errors.EmptyDataError) as error:
        raise ValueError("Unable to read CSV file.") from error

    if column not in data.columns:
        raise ValueError(f"Column not found: {column}")

    values = data[column].tolist()
    if not values:
        raise ValueError("CSV column must contain numbers.")

    return numeric_values(values)
