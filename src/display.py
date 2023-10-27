from solve import ft_sqrt


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


def display_coefficients(a: float, b: float, c: float,
                         discriminant: float | None):
    if discriminant is None:
        print(f"\na = {a}, b = {b}, c = {c}, x = ?")
    else:
        print(
            f"\na = {a}, b = {b}, c = {c}, discriminant:{discriminant}, x = ?")


def display_two_real_solutions(a: float, b: float, discriminant: float):
    print("\nsearching for two real solutions x1 and x2:")
    print("x1 = -b - discriminant² / 2 * a")
    print(f"x1 = -({b}) - {discriminant}² / 2 * {a}")
    print(f"x1 = {-b - ft_sqrt(discriminant)} / {2 * a}")
    print(f"x1 = {(-b - ft_sqrt(discriminant)) / (2 * a)}")
    print("\nx2 = -b + discriminant² / 2 * a")
    print(f"x2 = -({b}) + {discriminant}² / 2 * {a}")
    print(f"x2 = {-b + ft_sqrt(discriminant)} / {2 * a}")
    print(f"x2 = {(-b + ft_sqrt(discriminant)) / (2 * a)}")


def display_find_discriminant(a: float, b: float, c: float):
    print("\ndiscriminant = b² - 4 * a * c")
    print(f"discriminant = {b}² - 4 * {a} * {c}")
    print(f"discriminant = {b ** 2} - ({4 * a * c})")
    print(f"discriminant = {b ** 2 - 4 * a * c}")


def display_two_complex_solution_real_number(a: float, b: float):
    print('\nDiscriminant is negative: searching \
for two complex solutions x1 and x2:')
    print("real number = -b / 2 * a")
    print(f"real number = {b * -1} / 2 * {a}")
    print(f"real number = {b * -1} / {2 * a}")
    print(f"real number = {(b * -1) / (2 * a)}")


def display_two_complex_solution_imaginary_number(a: float, b: float,
                                                  discriminant: float,
                                                  coeff: int, radicant: int,
                                                  real_number: float,
                                                  imaginary_number: float):
    print("\nimaginary number = (√discriminant / 2 * a) * i")
    print(f"imaginary number = (√{discriminant} / 2 * {a}) * i")
    print("\nIs the discriminant reductible?")
    print(f"√{discriminant * -1} = {coeff}√{radicant}")
    print(
        f"imaginary number = ({coeff * ft_sqrt(radicant)} / {2 * a}) * i")
    print(
        f"imaginary number = ({(coeff * ft_sqrt(radicant)) / (2 * a)}) * i")
    print("\nx1 = real number + imaginary number")
    print(f"x1 = {real_number:.6f} + {imaginary_number:.6f}i")
    print("\nx2 = real number - imaginary number")
    print(f"x2 = {real_number:.6f} - {imaginary_number:.6f}i")
