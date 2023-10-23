import re
def split_expression(expression: str) -> str:
    splitted = expression.split('=', 1)
    return splitted[0], splitted[1]

def get_coefficients_list(expression: str) -> list[float]:
    # # split
    split_pattern = r'(\+|\-)'
    terms = re.split(split_pattern, expression)
    # # trim string
    terms = list(map(lambda term: term.replace(" ", ""), terms))
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
        if term and term == '+' or term =='-':
            operator = term
    coefficients_list = []
    
    for term in terms_with_operator:
        coefficient_end = term.find('*')
        value = float(term[0:coefficient_end])
        degree = int(term[-1:])
        if degree >= len(coefficients_list):
            coefficients_list.append([value])
        else:
            coefficients_list[degree].extend([value])       
    return coefficients_list

def calculate_to_reduce(expression: list):
    reduced_list = [[] for x in range(len(expression))]
    res = 0
    index = -1
    for degree in expression:
        res=0
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
    print(left)
    

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

    index = -1
    for degree in right_reduced:
        index += 1
        jindex = -1
        for value in degree:
            
            right_reduced[index][jindex] =value * -1
            jindex +=1
            print(value)
        # index +=1

    print('after * -1', right_reduced)
    print(f"left reduced: {left_reduced} right reduced: {right_reduced}")
    create_equation(left_reduced, right_reduced)
    print(f"left reduced: {left_reduced} right reduced: {right_reduced}")
    
    left_reduced = calculate_to_reduce(left_reduced)
    print(f"left reduced: {left_reduced} right reduced: {right_reduced}")
    return left_reduced

def display_reduced_expression(expression: str):
    to_display = ""
    index = -1
    # for degree in expression:
    #     index += 1
    #     for value in degree: 