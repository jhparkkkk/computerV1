
def solve_constant_equation(equation: list[float]) -> str:
    if equation[0][0] == 0.0:
        return "The equation is true for any real numbers X"
    return "There is no real X that can satisfy this equation"

def solve_linear_equation(equation: list[float]) -> str:
    a = equation[1][0]
    b = equation[0][0]
    x = -b / a 
    return "The solution is:\n" + str(x)

def ft_sqrt(value: float):
    return value ** (0.5)

def find_discriminant(a: float, b: float, c:float) -> float:
    res = (b ** 2) - (4 * a * c)
    print('discriminant', res)
    return res

def find_two_real_solutions(a: float, b: float, discriminant: float):
    x1 = (-b - ft_sqrt(discriminant)) / (2 * a)
    x2 = (-b + ft_sqrt(discriminant)) / (2 * a)
    print(x1, x2)
    return x1, x2

def find_one_real_solution(a: float, b: float):
    x = (-b) / (2*a)
    return x

def perfect_square(value):  
    # Returns list of perfect squares less than or equal to n 
    accumulation_list = [1]
    index, increment = 0, 3
    while accumulation_list[-1]+increment <= value:
        accumulation_list.append(accumulation_list[index]+increment) # Add increment to get next perfect square
        index += 1 
        increment = 2*index+3
    print('list', accumulation_list)

    return accumulation_list

def reducesqrt(n):
    factors = []
    perfect_squares = perfect_square(n)[::-1]
    for square in perfect_squares:
        if n % square == 0:
            factors.append(square)
            break
    print('factors', factors) 
    if len(factors)==0:
        print('\u221A',n) # Square root is irreducible
    else:
        print('max(factors)', factors[0])
        a = int(ft_sqrt(factors[0])) # Coefficient
        b = int(n/max(factors)) # Argument of the square root
        print(a,'\u221A',b) # Reduced square root
        return a, b

def find_two_complex_solutions(a: float, b: float, coefficient: int, radicant: int):
    real_number = (-b/(2*a))
    imaginary_number = ( (coefficient*(ft_sqrt(radicant))) / (2*a))
    x1 = f"{real_number:.6f} + {imaginary_number:.6f}i"
    x2 = f"{real_number:.6f} - {imaginary_number:.6f}i"
    return x1, x2
    # return f"Discriminant is strictly negative, the two solutions are:\n{x1}\n{x2}"


def solve_quadratic_equation(equation: list[float]):
    a = equation[2][0]
    b = equation[1][0]
    c = equation[0][0]
    print(f"a: {a}, b: {b}, c:{c}")
    discriminant = find_discriminant(a, b, c)
    if discriminant > 0:
        x1, x2 = find_two_real_solutions(a, b, discriminant)
        return f"Discriminant is strictly positive, the two solutions are:\n{x1:.6f}\n{x2:.6f}"
    elif discriminant == 0:
        x = find_one_real_solution(a, b)
        return f"Discriminant is equal to zero, the solution is:\n{x:.6f}"

    elif discriminant < 0:
        coefficient, radicant = reducesqrt(discriminant * -1)
        print(discriminant)
        x1, x2 = find_two_complex_solutions(a, b, coefficient, radicant)
        return f"Discriminant is strictly negative, the two solutions are:\n{x1}\n{x2}"

    pass

def solve(equation: list[float], degree: int):
    solve_dict = {
        0: solve_constant_equation,
        1: solve_linear_equation,
        2: solve_quadratic_equation
    }

    if degree in solve_dict:
        solution = solve_dict[degree](equation)
    else:
        raise Exception('The polynomial degree is strictly greater than 2, I can\'t solve.')
    
    print(solution)

# x^2 - 6x + 9 