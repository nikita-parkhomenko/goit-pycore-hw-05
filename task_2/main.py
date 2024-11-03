import re
from typing import Callable, Generator


def generator_numbers(text: str) -> Generator[float, None, None]:
    # regular expression to find numbers in the text
    pattern = r"\b\d+\.\d+\b"
    # iterate over all matches and yield as floats
    for match in re.findall(pattern, text):
        yield float(match)


def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    # use generator function to sum all the values
    return sum(func(text))


# example usage
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income:.2f}")
