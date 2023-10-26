import sys as sys
import parsing_utils as parser
from colorama import Fore
import display
import solve


def main():
    try:
        assert len(sys.argv) == 2, 'one argument required'
        print(
            Fore.BLUE, f"✏️  initial expression: {sys.argv[1]}\n", Fore.RESET)
        left_expression, right_expression = parser.split_expression(
            sys.argv[1])
        print(Fore.CYAN, f"   left expression:|{left_expression}|",
              Fore.YELLOW, f"right expression: {right_expression}")

        # terms list
        left_terms = parser.create_terms_list(left_expression)
        right_terms = parser.create_terms_list(right_expression)
        print(Fore.CYAN, f"   left terms:|{left_terms}|",
              Fore.YELLOW, f"right terms: {right_terms}")

        # check pattern
        if parser.check_term_pattern(left_terms) == False or parser.check_term_pattern(right_terms) == False:
            raise Exception(
                'invalid format: expression must be digits|*|X|^|digits')

        # degree
        degree = parser.get_degree(left_terms, right_terms)
        print('degree is', degree)

        left_coefficient_list = parser.get_coefficients_list(
            left_terms, degree)
        right_coefficient_list = parser.get_coefficients_list(
            right_terms, degree)
        print(Fore.CYAN, f"   left coefficient: {left_coefficient_list}",
              Fore.YELLOW, f"right list: {right_coefficient_list}", Fore.RESET)

        # reduce expression
        reduced_expression = parser.reduce_expression(
            left_coefficient_list, right_coefficient_list)
        print(f"Reduced form: {reduced_expression}")
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
