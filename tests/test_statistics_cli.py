
"""Tests for statistics and CSV commands in the CLI."""

import pytest

from calculator.cli import read_values, run


def simulate(monkeypatch, capsys, commands):
    inputs = iter(commands)
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    run()
    return capsys.readouterr().out


@pytest.mark.parametrize(
    "command, numbers, expected",
    [
        ("sum", "1,2,3", "Result: 6"),
        ("mean", "2,4,6", "Result: 4"),
        ("stddev", "2,4,6", "Result: 2"),
    ],
)
def test_statistics_cli(monkeypatch, capsys, command, numbers, expected):
    output = simulate(
        monkeypatch, capsys, [command, numbers, "exit"]
    )
    assert expected in output


def test_invalid_statistics_cli(monkeypatch, capsys):
    output = simulate(
        monkeypatch, capsys, ["mean", "abc,2", "exit"]
    )
    assert "Error:" in output


def test_csv_mean_cli(monkeypatch, capsys, tmp_path):
    path = tmp_path / "numbers.csv"
    path.write_text("score\n2\n4\n6\n", encoding="utf-8")

    output = simulate(
        monkeypatch, capsys,
        ["csv mean", str(path), "score", "exit"]
    )
    assert "Result: 4" in output


def test_csv_stddev_cli(monkeypatch, capsys, tmp_path):
    path = tmp_path / "numbers.csv"
    path.write_text("score\n2\n4\n6\n", encoding="utf-8")

    output = simulate(
        monkeypatch, capsys,
        ["csv stddev", str(path), "score", "exit"]
    )
    assert "Result: 2" in output


def test_invalid_csv_cli(monkeypatch, capsys, tmp_path):
    output = simulate(
        monkeypatch, capsys,
        ["csv mean", str(tmp_path / "missing.csv"), "score", "exit"]
    )
    assert "Error:" in output


def test_read_values_empty_input(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "")
    with pytest.raises(ValueError):
        read_values()

def test_statistics_cli_rejects_insufficient_values(monkeypatch, capsys):
    output = simulate(
        monkeypatch,
        capsys,
        ["stddev", "5", "exit"],
    )

    assert "Error: At least two numbers are required." in output

def test_statistics_cli_rejects_invalid_number_list(monkeypatch, capsys):
    output = simulate(
        monkeypatch,
        capsys,
        ["mean", "", "exit"],
    )

    assert "Error:" in output
