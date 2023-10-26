import sys as sys
import parsing_utils as parser
from colorama import Fore
import display
import solve


def main():
    try:
        assert len(sys.argv) == 2, 'one argument required'
        print(f"initial expression: {sys.argv[1]}")
        left_expression, right_expression = parser.split_expression(
            sys.argv[1])
        display.display_left_and_right(left_expression, right_expression)
        left_terms = parser.create_terms_list(left_expression)
        right_terms = parser.create_terms_list(right_expression)
        display.display_left_and_right(left_terms, right_terms)
        # check pattern
        if parser.check_term_pattern(left_terms) == False or parser.check_term_pattern(right_terms) == False:
            raise Exception(
                'invalid format: expression must be digits|*|X|^|digits')

        # degree
        degree = parser.get_degree(left_terms, right_terms)

        left_coefficients = parser.get_coefficients_list(
            left_terms, degree)
        right_coefficients = parser.get_coefficients_list(
            right_terms, degree)
        display.display_left_and_right(
            left_coefficients, right_coefficients)

        # reduce expression
        reduced_expression = parser.reduce_expression(
            left_coefficients, right_coefficients)
        # display
        display.display_reduced_expression(reduced_expression)
        display.display_polynomial_degree(degree)
        # calcul
        solve.solve(reduced_expression, degree)
    except AssertionError as error:
        print(f"error: {error}")
    except Exception as error:
        print(Fore.LIGHTMAGENTA_EX, f"🐥 {error}")


if __name__ == "__main__":
    main()
