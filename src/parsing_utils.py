import re


def split_expression(expression: str) -> str:
    """split the initial expression using '=' sign to
return left-sided expression and right-sided expression. The expressed get trimmed
    Args:
        expression (str): expression describing a polynomial equation

    Raises:
        ValueError: missing '=' signs meaning is not an equation
        ValueError: if one sided expression is empty meaning
        initial expression was incomplete

    Returns:
        str: left-sided expression and right-sided expression
    """
    splitted = expression.split('=')
    if len(splitted) != 2:
        raise ValueError('missing or too many equal operator')
    splitted = [re.sub(r'[\s]', '', term) for term in splitted]
    if len(splitted[0]) == 0 or len(splitted[1]) == 0:
        raise ValueError('expression is not complete')
    return splitted[0], splitted[1]


def create_terms_list(expression: str) -> list[str]:
    # split
    split_pattern = r'(\+|\-)'
    terms = re.split(split_pattern, expression)
    terms_with_operator = []
    if terms[0] and terms[0][0].isdigit():
        terms[0] = '+' + terms[0]
        terms_with_operator.append(terms[0])
    
    operator = ''
    # append positive or negative sign to each coefficient
    for term in terms:
        if operator != '':
            if term != "+" and term != '-':
                terms_with_operator.append(operator + term)
        if term and term == '+' or term == '-':
            operator = term
    return terms_with_operator

def get_degree(left_terms: list[str], right_terms: list[str]) -> int:
    left_degree = 0
    for term in left_terms:
        exponent = int(term[-1:])
        if exponent > left_degree:
            left_degree = exponent
    right_degree = 0
    for term in right_terms:
        exponent = int(term[-1:])
        if exponent > right_degree:
            right_degree = exponent
    if left_degree > right_degree:
        return left_degree
    return right_degree

def get_coefficients_list(terms: list[str], degree: int) -> list[float]:
    print('terms:', terms)
    coefficients_list = [[] for i in range(degree + 1)]
    # coefficients_list = []
    
    for term in terms:
        coefficient_end = term.find('*')
        if coefficient_end == -1 and term == '+0':
            value = 0
        # print('term', term, 'coefficient end', coefficient_end)
        else:
            value = float(term[0:coefficient_end])
        degree = int(term[-1:])
        coefficients_list[degree].extend([value])

    # print('coefficient list:', coefficients_list)
    return coefficients_list


def calculate_to_reduce(expression: list):
    reduced_list = [[] for x in range(len(expression))]
    res = 0
    index = -1
    for degree in expression:
        res = 0
        index += 1
        for value in degree:
            res += value
        reduced_list[index].extend([res])
    return reduced_list


def create_equation(left: list[float], right: list[float]):
    index = -1
    for degree in right:
        index += 1
        for value in degree:
            left[index].extend([value])


def negate_expression(expression: list[float]) -> list[float]:
    i = -1
    for degree in expression:
        i += 1
        j = -1
        for value in degree:
            expression[i][j] = value * -1
            j += 1


def reduce_expression(left: list[float], right: list[float]) -> list[float]:
    if len(left) > len(right):
        size = len(left)
    else:
        size = len(right)
    reduced_list = [[] for x in range(size)]
    res = 0
    index = -1
    left_reduced = calculate_to_reduce(left)
    right_reduced = calculate_to_reduce(right)

    negate_expression(right_reduced)

    print('negate right expression:', right_reduced)
    print(f"left reduced: {left_reduced} right reduced: {right_reduced}")
    create_equation(left_reduced, right_reduced)
    print(f"equation: {left_reduced}")

    left_reduced = calculate_to_reduce(left_reduced)
    print(f"reduced equation: {left_reduced}")
    return left_reduced


