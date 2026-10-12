
"""Read, evaluate, print, and loop until the user exits."""

from math import isfinite

from calculator.factory import CalculationFactory
from calculator.history import History


HELP = """Commands:
  add       Add two numbers
  subtract  Subtract the second number from the first
  history   Show this session's calculations
  remove    Remove a calculation by its displayed number
  help      Show available commands
  exit      Exit the calculator"""


def show_history(history: History) -> None:
    """Display saved calculations without recalculating results."""
    calculations = history.get_history()
    results = history.get_results()

    if not calculations:
        print("No calculations in history.")
        return

    print("Calculation History\n")

    for number, (calculation, result) in enumerate(
        zip(calculations, results), start=1
    ):
        print(
            f"{number}. {type(calculation).__name__}: "
            f"{calculation.a:g}, {calculation.b:g} = {result:g}"
        )


def read_number(prompt: str) -> float:
    """Convert terminal text into a finite floating-point number."""
    number = float(input(prompt))

    if not isfinite(number):
        raise ValueError("A finite number is required.")

    return number


def run() -> None:
    """Run one independent calculator session."""
    history = History()
    operations = {"add", "subtract"}

    print('OOP Calculator\n\nType "help" for commands.')

    while True:
        try:
            command = input("> ").strip().lower()

            if command == "exit":
                break

            if command in operations:
                try:
                    a = read_number("First number: ")
                    b = read_number("Second number: ")

                    calculation = CalculationFactory.create(
                        command, a, b
                    )
                    result = calculation.get_result()

                except ValueError:
                    print(
                        "Invalid number or result. "
                        "Please use finite numbers."
                    )
                    continue

                history.add(calculation, result)
                print(f"Result: {result:g}")

            elif command == "history":
                show_history(history)

            elif command == "remove":
                show_history(history)

                if not history.get_history():
                    continue

                try:
                    number = int(
                        input("Enter calculation number to remove: ")
                    )

                    if number < 1:
                        raise IndexError("History index out of range")

                    saved_result = history.get_results()[number - 1]
                    removed = history.remove(number - 1)

                except ValueError:
                    print("Please enter a whole calculation number.")

                except IndexError:
                    print("Calculation does not exist.")

                else:
                    print(
                        f"Removed: {type(removed).__name__}: "
                        f"{removed.a:g}, {removed.b:g} = {saved_result:g}"
                    )

            elif command == "help":
                print(HELP)

            else:
                print(
                    'Unknown command.\n'
                    'Type "help" for available commands.'
                )

        except (EOFError, KeyboardInterrupt):
            print()
            break

    print("Goodbye!")
