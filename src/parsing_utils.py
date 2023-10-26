import re


def split_expression(expression: str) -> str:
    """split the initial expression using '=' sign as a delimiter to
return left-sided expression and right-sided expression. The expression get trimmed
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
    """from expression, create a list of subdivided expressions following
the pattern ax^b

    Args:
        expression (str): right-sided or left-sided expression

    Raises:
        ValueError: missing an operator

    Returns:
        list[str]: list of terms
    """
    # split expression using add substract operators as delimiters
    split_pattern = r'(\+|\-)'
    terms = re.split(split_pattern, expression)

    # verify any missing operator by counting occurences
    # of character 'X'
    for term in terms:
        if term.count('X') > 1:
            raise ValueError('expression format is invalid')

    terms_with_operator = []
    # if first number is positive and operator is missing, append
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


def check_term_pattern(terms: list[str]) -> bool:
    """use regex to check ax^b pattern

    Args:
        terms (list[str]): the list of subdivided expressions

    Returns:
        bool: false if term does not match the regex pattern
    """
    if len(terms) == 1 and terms[0] == '+0':
        return True
    # sign | digits | * | X | ^ | digits
    pattern = r"^[+-][0-9].*\*X\^[0-9]+$"

    for term in terms:
        if re.match(pattern, term) == None:
            return False
    return True


def get_degree(left_terms: list[str], right_terms: list[str]) -> int:
    """returns degree of the equation by searching the highest exponent 

    Args:
        left_terms (list[str]): left-sided expression
        right_terms (list[str]): right-sided expression

    Returns:
        int: degree
    """
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
    """convert list[str] to list[float]. Extract coefficients from each term
index of list is related to coefficient's exponent value.
if coefficient * X ^ 2 then coefficient is appended in coefficient[2]
    Args:
        terms (list[str]): where to extract coefficients
        degree (int): to create a list of degree + 1 size 

    Returns:
        list[float]: list of coefficient
    """
    coefficients_list = [[] for i in range(degree + 1)]

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


def calculate_to_reduce(expression: list[float]) -> list[float]:
    """from coefficient list of lists, if sub-list is greater than size 1, means
coefficients needs to be calculated in order to reduce the expression

    Args:
        expression (list): list of list of coefficients

    Returns:
        list[float]: list of reduced coefficients
    """
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
    """extend left-sided coefficients values with right-sided
coefficients value

    Args:
        left (list[float]): left-sided coefficients values
        right (list[float]): right-sided coefficients values
    """
    index = -1
    for degree in right:
        index += 1
        for value in degree:
            left[index].extend([value])


def negate_expression(expression: list[float]) -> list[float]:
    """negate right sided expression to create equation:
equation = 0

    Args:
        expression (list[float]): coefficients to negate

    Returns:
        list[float]: negated coefficients
    """
    i = -1
    for degree in expression:
        i += 1
        j = -1
        for value in degree:
            expression[i][j] = value * -1
            j += 1


def reduce_expression(left: list[float], right: list[float]) -> list[float]:
    """reduce expression to solve equation. Both side, coefficients with the same exponent value
are calculated. Then the riht-sided coefficient are first negated and then added to the left-sided 

    Args:
        left (list[float]): left-sided equation
        right (list[float]): right-sided equation

    Returns:
        list[float]: reduced expression
    """
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
