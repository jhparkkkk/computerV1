def display_reduced_expression(expression: list[float]):
    """display reduced expression

    Args:
        expression (list[float]): coefficients values
    """
    to_display = "Reduced form: "
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
    print("Polynomial degree: " + str(degree))
