"""Math exercises."""
import math


def sum_and_difference(num_a: int, num_b: int) -> tuple:
    """Return the sum and difference of given variables num_a and num_b."""
    sum = num_a + num_b
    difference = num_a - num_b
    return sum, difference


def float_division(num_a: int, num_b: int) -> float:
    """Divide given variables num_a and num_b and return the result."""
    division = num_a / num_b
    return division


def integer_division(num_a: int, num_b: int) -> int:
    """Divide given variables num_a and num_b and return the result rounded down."""
    division = num_a // num_b
    return division


def powerful_operations(num_a: int, num_b: int) -> tuple:
    """Return the product of given variables, num_a to the power of num_b and the remainder of division of variables."""
    multiply_numbers = num_a * num_b
    power = num_a ** num_b
    remainder = num_a % num_b
    return multiply_numbers, power, remainder


def find_average(num_a: int, num_b: int) -> float:
    """Return the average of given variables."""
    average = (num_a + num_b) / 2
    return average


def area_of_a_circle(radius: float) -> float:
    """Calculate and return the area of a circle."""
    circle_area = round((math.pi * radius ** 2), 2)
    return circle_area


def area_of_an_equilateral_triangle(side_length: float) -> int:
    """Calculate and return the area of an equilateral triangle."""
    triangle_area = int(round(math.sqrt(3) / 4 * side_length ** 2, 0))
    return triangle_area


def calculate_discriminant(a: int, b: int, c: int) -> int:
    """Calculate discriminant with given variables and return the result."""
    discriminant = b ** 2 - 4 * a * c
    return discriminant


def calculate_hypotenuse_length(a: int, b: int) -> float:
    """Return the length of hypotenuse when the lengths of the catheti are given."""
    c = math.sqrt(a ** 2 + b ** 2)
    return c


def calculate_cathetus_length(a: int, c: int) -> float:
    """Return the length of cathetus when the lengths of the second cathetus and hypotenuse are given."""
    b = math.sqrt(c ** 2 - a ** 2)
    return b


if __name__ == '__main__':
    # assert sum_and_difference(5, 6) == (11, -1)
    # assert sum_and_difference(11, 9) == (20, 2)
    # print("OK!")
    print(sum_and_difference(5, 6), "== (11, -1)")
    print(sum_and_difference(11, 9), "== (20, 2)")

    print(float_division(10, 2), "== 5.0")
    print(float_division(4, 2), "== 2.0")

    print(integer_division(3, 2), "== 1")
    print(integer_division(44, 33), "== 1")

    print(powerful_operations(3, 2), "== (6, 9, 1)")
    print(powerful_operations(5, 4), "== (20, 625, 1)")

    print(find_average(2, 6), "== 4.0")
    print(find_average(999, 999), "== 999.0")

    print(round(area_of_a_circle(5), 2), "== 78,54")
    print(round(area_of_a_circle(13), 2), "== 530,54")

    print(area_of_an_equilateral_triangle(4))
    print(area_of_an_equilateral_triangle(10))
