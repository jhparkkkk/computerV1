import display as dp


def solve_constant_equation(equation: list[float]) -> str:
    """verify if constant value is equal to zero

    Args:
        equation (list[float]): coefficients list

    Returns:
        str: result
    """
    if equation[0][0] == 0.0:
        print(f"a = {equation[0][0]}")
        return "The equation is true for any real numbers X"
    return "There is no real X that can satisfy this equation"


def solve_linear_equation(equation: list[float]) -> str:
    """find x by calculating -b / a

    Args:
        equation (list[float]): coefficients list

    Returns:
        str: result
    """
    try:
        a = equation[1][0]
        b = equation[0][0]
        if a == 0.0 and b == 0.0:
            return "The equation is true for any real numbers X"
        x = -b / a

        print(f"\na = {a} b = {b} x = ?\nx = -b / a\nx = {-b} / {a}\nx = {x}")
        return "\nThe solution is:\n" + str(x)
    except Exception as error:
        print(error)
        return "\nThere is no solution"


def ft_sqrt(value: float):
    """calculate square root of value by calculating value power 0.5

    Args:
        value (float): value to operate on

    Returns:
        float: result
    """
    return value ** (0.5)


def find_discriminant(a: float, b: float, c: float) -> float:
    """to determine number of solution, need to calculate the discriminant.
the discriminant is the value that derivate from a, b and c.
D=b^2 −4ac
    Args:
        a (float): coefficient a
        b (float): coefficient b
        c (float): coefficient c

    Returns:
        float: discriminant
    """
    dp.display_find_discriminant(a, b, c)
    res = (b ** 2) - (4 * a * c)
    return res


def find_two_real_solutions(a: float, b: float, discriminant: float):
    """if the discriminant is positive
 then there are 2 solutions with real numbers

    Args:
        a (float): coefficient a
        b (float): coefficient b
        discriminant (float): discriminant

    Returns:
        float: value of x1
        float: value of x2

    """
    try:
        x1 = (-b - ft_sqrt(discriminant)) / (2 * a)
        x2 = (-b + ft_sqrt(discriminant)) / (2 * a)
        dp.display_two_real_solutions(a, b, discriminant)
        return x1, x2
    except Exception as error:
        raise (error)


def find_one_real_solution(a: float, b: float):
    """if discriminant is equal to zero the equation
has one real solution(repeated root)

    Args:
        a (float): coefficient a
        b (float): coefficient b

    Returns:
        float: value of x
    """
    try:
        x = (-b) / (2*a)
        return x
    except Exception as error:
        raise (error)


def perfect_square(value: int) -> list[int]:
    """find perfect square that are less than value

    Args:
        value (int): value to limit perfect square finding

    Returns:
        list[int]: list of perfect square
    """
    # Returns list of perfect squares less than or equal to n
    accumulation_list = [1]
    index, increment = 0, 3
    while accumulation_list[-1]+increment <= value:
        # Add increment to get next perfect square
        accumulation_list.append(accumulation_list[index]+increment)
        index += 1
        increment = 2*index+3
    return accumulation_list


def reduce_square(value):
    """factorize square value. First search for perfect square that are below n

    Args:
        value (): _description_

    Returns:
        coefficient, radicant (int): coeffcient and radicant
of the reduced square
    """
    factors = []
    perfect_squares = perfect_square(value)[::-1]
    for square in perfect_squares:
        if value % square == 0:
            factors.append(square)
            break
    # Square root is irreducible
    if len(factors) == 0:
        return 1, value
    # return reduced square root
    else:
        coefficient = int(ft_sqrt(factors[0]))
        radicant = int(value/factors[0])
        return coefficient, radicant


def find_two_complex_solutions(a: float, b: float, discriminant: float):
    """if the discriminant is negative then the equation has no real solutions
but instead has two complex (or imaginary) solutions.

    Args:
        a (float): coefficient a
        b (float): coefficient b
        coefficient (int): coefficient of the discriminant
        radicant (int): radicant of the discriminant

    Returns:
        _type_: _description_
    """
    try:
        dp.display_two_complex_solution_real_number(a, b)
        real_number = (-b/(2*a))
        coefficient, radicant = reduce_square(discriminant * -1)
        imaginary_number = ((coefficient*(ft_sqrt(radicant))) / (2*a))
        dp.display_two_complex_solution_imaginary_number(
            a, b, discriminant, coefficient, radicant,
            real_number, imaginary_number)

        x1 = f"{real_number:.6f} + {imaginary_number:.6f}i"
        x2 = f"{real_number:.6f} - {imaginary_number:.6f}i"
        return x1, x2
    except Exception as error:
        raise (error)


def solve_quadratic_equation(equation: list[float]):
    """first calculate the discriminant.
If discriminant > 0 the equation has two distinct real solutions.
If discriminant = 0 the equation has one real solution (a repeated root).
If discriminant < 0 the equation has no real solutions but instead has
two complex (or imaginary) solutions.

    Args:
        equation (list[float]): coefficients a, b, c

    Returns:
        str: solution
    """
    a = equation[2][0]
    b = equation[1][0]
    c = equation[0][0]
    if a == 0.0 and b == 0.0 and c == 0.0:
        return "The equation is true for any real numbers X"
    dp.display_coefficients(a, b, c, None)
    discriminant = find_discriminant(a, b, c)
    dp.display_coefficients(a, b, c, discriminant)
    if discriminant > 0:
        x1, x2 = find_two_real_solutions(a, b, discriminant)
        return f"\nDiscriminant is strictly positive, \
the two solutions are:\n{x1:.6f}\n{x2:.6f}"
    elif discriminant == 0:
        x = find_one_real_solution(a, b)
        return f"\nDiscriminant is equal to zero, the solution is:\n{x:.6f}"

    elif discriminant < 0:
        x1, x2 = find_two_complex_solutions(a, b, discriminant)
        return f"\nDiscriminant is strictly negative, \
the two solutions are:\n{x1}\n{x2}"


def solve(equation: list[float], degree: int):
    """depending on the degree level, solve equation

    Args:
        equation (list[float]): coefficients list
        degree (int): degree level

    Raises:
        Exception: cannot solve above degree 2
    """
    solve_dict = {
        0: solve_constant_equation,
        1: solve_linear_equation,
        2: solve_quadratic_equation
    }

    if degree in solve_dict:
        solution = solve_dict[degree](equation)
    else:
        raise Exception(
            'The polynomial degree is strictly greater than 2, \
I can\'t solve.')
    print(solution)
