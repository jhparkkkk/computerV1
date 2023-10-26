from colorama import Fore


def display_reduced_expression(expression: list[float]):
    """display reduced expression

    Args:
        expression (list[float]): coefficients values
    """
    to_display = "\nReduced form: "
    index = -1
    for degree in expression:
        index += 1
        for value in degree:
            if int(value) == value:
                value = int(value)
            if value >= 0 and index != 0:
                operator = '+ '
            elif value < 0:
                value *= -1
                operator = '- '
            else:
                operator = ''
            to_display += operator + str(value) + ' * X^' + str(index) + ' '
    to_display += "= 0"
    print(to_display)


def display_polynomial_degree(degree: int):
    """display polynomial degree

    Args:
        degree (int): polynomial degree
    """
    print("\nPolynomial degree: " + str(degree))


def display_left_and_right(left: list[str | float], right: list[str | float]):
    print(f"\nleft: {left}\nright: {right}")


def display_coefficients(a: float, b: float, c: float, discriminant: float | None):
    if discriminant == None:
        print(f"\na = {a} ",  f"b = {b} ", f"c = {c} ")
    else:
        print(f"\na = {a} ",  f"b = {b} ",
              f"c = {c} ",  f"discriminant:{discriminant}")
