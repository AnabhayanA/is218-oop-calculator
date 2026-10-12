
"""Tests for reading CSV data."""

import pytest

from calculator.csv_reader import read_csv_numbers


def test_read_csv_numbers(tmp_path):
    path = tmp_path / "numbers.csv"
    path.write_text("score\n10\n20\n30\n", encoding="utf-8")

    assert read_csv_numbers(str(path), "score") == (10.0, 20.0, 30.0)


def test_csv_missing_path_or_column():
    with pytest.raises(ValueError, match="path and column"):
        read_csv_numbers("", "score")

    with pytest.raises(ValueError, match="path and column"):
        read_csv_numbers("numbers.csv", "")


def test_csv_file_missing(tmp_path):
    with pytest.raises(ValueError, match="Unable to read"):
        read_csv_numbers(str(tmp_path / "missing.csv"), "score")


def test_csv_empty_file(tmp_path):
    path = tmp_path / "empty.csv"
    path.write_text("", encoding="utf-8")

    with pytest.raises(ValueError, match="Unable to read"):
        read_csv_numbers(str(path), "score")


def test_csv_missing_column(tmp_path):
    path = tmp_path / "numbers.csv"
    path.write_text("score\n10\n", encoding="utf-8")

    with pytest.raises(ValueError, match="Column not found"):
        read_csv_numbers(str(path), "missing")


def test_csv_column_without_rows(tmp_path):
    path = tmp_path / "numbers.csv"
    path.write_text("score\n", encoding="utf-8")

    with pytest.raises(ValueError, match="must contain"):
        read_csv_numbers(str(path), "score")


def test_csv_invalid_number(tmp_path):
    path = tmp_path / "numbers.csv"
    path.write_text("score\n10\ninvalid\n", encoding="utf-8")

    with pytest.raises(ValueError, match="numeric"):
        read_csv_numbers(str(path), "score")
