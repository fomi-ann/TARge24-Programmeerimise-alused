"""Function examples."""


def func() -> None:
    """Print to console - 'I' m inside the function'."""
    print("I´m inside the function")


def my_name_is(name: str) -> None:
    """Print to console - 'My name is [name]'."""
    print(f"My name is {name}")


def sum_six(num: int):
    """Return sum of num and 6."""
    return num + 6


def sum_numbers(a: int, b: int):
    """Return sum of a and b."""
    return a + b


def usd_to_eur(dollar: int) -> float:
    """Convert dollar to euro."""
    return dollar * 0.8


if __name__ == '__main__':
    func()
    my_name_is("Anna")
    sum_numbers(1, 2)

a = 15

print(a % 3)
