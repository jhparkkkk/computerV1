import sys as sys
import parsing_utils as parser
from colorama import Fore


def main():
    try:
        assert len(sys.argv) == 2, 'one argument required'
        print(
            Fore.BLUE, f"✏️  initial expression: {sys.argv[1]}\n", Fore.RESET)
        left_expression, right_expression = parser.split_expression(
            sys.argv[1])
        print(Fore.CYAN, f"   left expression:|{left_expression}|",
              Fore.YELLOW, f"right expression: {right_expression}")
        left_coefficient_list = parser.get_coefficients_list(left_expression)
        right_coefficient_list = parser.get_coefficients_list(right_expression)
        print(Fore.CYAN, f"   left coefficient: {left_coefficient_list}",
              Fore.YELLOW, f"right list: {right_coefficient_list}", Fore.RESET)

        reduced_expression = parser.reduce_expression(
            left_coefficient_list, right_coefficient_list)
        print(f"Reduced form: {reduced_expression}")
        parser.display_reduced_expression(reduced_expression)
    except AssertionError as error:
        print(f"error: {error}")
    except Exception as error:
        print(Fore.LIGHTMAGENTA_EX, f"🐥 {error}")


if __name__ == "__main__":
    main()
