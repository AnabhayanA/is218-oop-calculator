
# OOP Calculator

A Python command-line calculator demonstrating object-oriented programming, composition, design patterns, statistics, CSV processing, automated testing, and continuous integration.

## Features

The calculator supports:

- Addition, subtraction, multiplication, and division
- Summation of multiple numbers
- Mean and sample standard deviation
- Statistical calculations from CSV files using pandas
- Calculation history and removal
- Input validation and error handling
- Interactive command-line interface

## Design Patterns

### Composition

Arithmetic calculations delegate their operations to reusable components instead of duplicating calculation logic.

### Factory Pattern

`CalculationFactory` creates calculation objects based on operation names.

Supported operations:

- `add`
- `subtract`
- `multiply`
- `divide`

### Command Pattern

`CalculateCommand` encapsulates arithmetic execution and saves successful calculations to history.

### Polymorphism

`Add`, `Subtract`, `Multiply`, and `Divide` implement the shared `Calculation` interface.

## Project Structure

```text
calculator/
    __init__.py
    __main__.py
    calculation.py
    cli.py
    commands.py
    composed_calculation.py
    csv_reader.py
    factory.py
    history.py
    operations.py
    statistics.py
    validation.py

tests/
    Automated tests for arithmetic, statistics,
    CSV processing, history, and CLI behavior.

.github/workflows/
    tests.yml

pytest.ini
requirements.txt
README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/AnabhayanA/is218-oop-calculator.git
cd is218-oop-calculator
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows Git Bash:

```bash
source venv/Scripts/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run the Calculator

```bash
python -m calculator
```

Available commands:

| Command | Description |
|---|---|
| `add` | Add two numbers |
| `subtract` | Subtract two numbers |
| `multiply` | Multiply two numbers |
| `divide` | Divide two numbers |
| `sum` | Sum multiple numbers |
| `mean` | Calculate the mean |
| `stddev` | Calculate sample standard deviation |
| `csv mean` | Calculate mean from a CSV column |
| `csv stddev` | Calculate standard deviation from a CSV column |
| `history` | Show saved arithmetic calculations |
| `remove` | Remove a saved calculation |
| `help` | Display available commands |
| `exit` | Exit the calculator |

## Example

```text
OOP Calculator

Type "help" for commands.

> multiply
First number: 6
Second number: 7
Result: 42

> mean
Enter numbers separated by commas: 10,20,30
Result: 20

> history
Calculation History

1. Multiply: 6, 7 = 42

> exit
Goodbye!
```

## CSV Support

Create a CSV file containing numeric values:

```csv
value
10
20
30
40
```

Run the calculator and enter:

```text
> csv mean
CSV file path: sample.csv
Column name: value
Result: 25
```

CSV processing uses pandas.

## Testing

Run the automated tests:

```bash
python -m pytest -q
```

Latest local test result:

- 116 tests passed
- 100% line and branch coverage
- Python 3.13.15

Coverage is enforced through `pytest.ini`.

## Continuous Integration

GitHub Actions runs the test suite on:

- Python 3.11
- Python 3.12
- Python 3.13
- Python 3.14

The workflow runs on pushes, pull requests, and manual execution.

## Error Handling

The calculator handles invalid numeric input, non-finite values, division by zero, unsupported operations, invalid CSV data, invalid history indices, and interrupted input.

Failed arithmetic calculations are not saved to history.

## Project Summary

This project demonstrates how composition, polymorphism, Factory and Command patterns, and modular testing can be combined in a maintainable Python application.

Automated tests and GitHub Actions help verify that new functionality does not break existing behavior.
