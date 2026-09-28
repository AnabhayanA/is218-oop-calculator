# OOP Calculator

This project is a command-line calculator built in Python to practice object-oriented programming, automated testing, error handling, and continuous integration.

The calculator supports addition, subtraction, calculation history, removing previous calculations, help commands, and clean program exit.

## Features

The calculator supports these commands:

- `add` — add two numbers
- `subtract` — subtract the second number from the first
- `history` — display calculations from the current session
- `remove` — remove a calculation from history
- `help` — display available commands
- `exit` — close the calculator

The calculator also handles invalid input without crashing. Invalid calculations are not added to history.

## Project Structure

```text
calculator/
    __init__.py
    __main__.py
    calculation.py
    cli.py
    history.py

tests/
    test_calculation.py
    test_cli.py
    test_history.py

.github/
    workflows/
        tests.yml

.gitignore
pytest.ini
requirements.txt
README.md
```

## Installation

Clone the repository and move into the project folder.

```bash
git clone git@github.com:AnabhayanA/is218-oop-calculator.git
cd is218-oop-calculator
```

Create a virtual environment:

```bash
python -m venv venv
```

On Windows PowerShell, activate it with:

```powershell
.\venv\Scripts\Activate.ps1
```

Install the required testing dependencies:

```bash
python -m pip install -r requirements.txt
```

## Running the Calculator

Start the calculator with:

```bash
python -m calculator
```

Example session:

```text
OOP Calculator

Type "help" for commands.
> add
First number: 10
Second number: 5
Result: 15
> subtract
First number: 20
Second number: 7
Result: 13
> history
Calculation History

1. Add: 10, 5 = 15
2. Subtract: 20, 7 = 13
> exit
Goodbye!
```

## Running Tests

Run the full test suite with:

```bash
python -m pytest
```

The project currently has 41 passing tests.

The `pytest.ini` configuration also requires 100% line and branch coverage.

A successful run should show:

```text
41 passed
Required test coverage of 100% reached.
```

## Main Design

The calculator separates different responsibilities into different parts of the program.

### Calculation

`Calculation` is an abstract base class that defines the common `get_result()` method.

`Add` and `Subtract` inherit from `Calculation` and provide their own implementation of `get_result()`.

This allows other parts of the program to work with calculation objects through the same interface instead of checking which exact operation each object represents.

### Polymorphism

Both `Add` and `Subtract` can be treated as `Calculation` objects.

For example:

```python
calculation.get_result()
```

works regardless of whether the object is an `Add` or `Subtract`.

The caller does not need separate logic for each type.

### History

`History` is responsible for storing calculation objects.

It can:

- add calculations
- return the current history
- remove calculations
- reject objects that are not calculations

The arithmetic itself does not belong inside `History`.

### CLI

The CLI handles user interaction.

It is responsible for:

- reading commands
- reading numeric input
- creating calculation objects
- displaying results
- showing history
- handling invalid input
- handling Ctrl+C and end-of-input

Separating the CLI from the calculation classes keeps user-interface logic away from the arithmetic logic.

## Error Handling

The calculator handles several invalid situations without crashing, including:

- invalid numeric input
- `nan`
- positive or negative infinity
- overflowing results
- invalid history removal numbers
- invalid removal text
- unknown commands
- Ctrl+C
- end-of-input

A failed calculation is not added to history.

## Continuous Integration

GitHub Actions automatically runs the project tests whenever code is pushed, a pull request is created, or the workflow is started manually.

The workflow tests the calculator using:

- Python 3.11
- Python 3.12
- Python 3.13
- Python 3.14

Each CI job:

1. downloads the repository
2. installs Python
3. installs packages from `requirements.txt`
4. runs `python -m pytest`

The same 100% coverage requirement used locally is enforced in CI.

## Stage 6 Reflection

### 1. Where would Multiply belong?

If I added multiplication, I would create a new `Multiply` class that inherits from `Calculation`.

It would implement `get_result()` the same way `Add` and `Subtract` do, except it would multiply the two operands.

I would also need to update the CLI so `multiply` is registered in the operations dictionary and add the command to the help text. I would add tests for multiplication results and tests showing that it works correctly through the CLI.

`History` would not need multiplication-specific logic. History already works with the common `Calculation` type. As long as `Multiply` follows the same contract, History can store it the same way it stores `Add` and `Subtract`.

This shows why using an abstraction is useful. New calculation types can be added without rewriting the collection that stores them.

### 2. What could email and text notifications share?

`EmailNotification` and `TextNotification` could share a common notification contract with a method such as:

```python
send()
```

The caller should only need to know that the notification object can send a message.

Each implementation would handle the details differently. An email notification might use an email address and email service, while a text notification might use a phone number and SMS service.

The caller would not need separate logic for every notification type as long as each object follows the same `send()` contract.

This is similar to how the calculator calls `get_result()` on different calculation objects.

### 3. What transfers to another programming language?

The main design ideas from this project can transfer to other programming languages.

These include:

- separating responsibilities
- classes and objects
- inheritance
- abstraction
- polymorphism
- using common interfaces or contracts
- encapsulating collections
- testing behavior
- handling errors
- continuous integration

The exact syntax will change depending on the language.

For example, Java might use interfaces differently, C# uses keywords such as `abstract`, `virtual`, and `override`, and JavaScript uses prototype-based inheritance underneath its class syntax.

I would still need to learn the syntax, type system, visibility rules, inheritance rules, error handling, and runtime behavior of the new language.

The design questions remain useful even when the language changes.

## Investigating CI Failures

If GitHub Actions fails, I would first identify which step failed.

If dependency installation fails, I would check `requirements.txt` and the installation error.

If a test fails, I would look for the first failed test and assertion instead of only reading the final exit-code message.

For example, I could reproduce one failed test locally with:

```bash
python -m pytest tests/test_calculation.py -k test_add
```

If the tests pass but coverage fails, I would look at the coverage report's `Missing` column. That would show which line or branch was not executed.

I would then determine what behavior is missing from the tests and add a meaningful test that exercises that path instead of excluding the code from coverage.

## README Usability Check

When following the README from a fresh environment, one instruction that can be confusing is virtual-environment activation because the command depends on the operating system.

For that reason, this README explicitly includes the Windows PowerShell activation command used for this project.

A new user should be able to clone the repository, create the environment, install dependencies, run the calculator, and run the tests using the instructions above.

## What I Learned

This project showed how a program can grow in small stages without putting every responsibility into one file.

The calculation classes handle arithmetic, History manages stored calculations, and the CLI handles interaction with the user.

Tests protect previous behavior while new functionality is added. Coverage helps reveal paths that have not been tested, but passing coverage alone does not prove that the program is correct.

GitHub Actions adds another level of confidence by running the same checks in fresh environments instead of depending only on my local computer.