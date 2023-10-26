
import unittest as ut
import sys
import os

from src.parsing_utils import *
from src.solve import solve_quadratic_equation


class TestParsing(ut.TestCase):
    #
    # split_expression(expression: str) -> str
    #
    def test_split_expression(self):
        self.assertEqual(split_expression(
            "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"), ("5*X^0+4*X^1-9.3*X^2", "1*X^0"))
        self.assertEqual(split_expression(
            "5 * X^0 + 4 * X^1 = 4 * X^0"), ("5*X^0+4*X^1", "4*X^0"))

    def test_invalid_equal_operator(self):
        with self.assertRaises(ValueError) as cm:
            split_expression("5 * X^0 + 4 * X^1")
        self.assertEqual(str(cm.exception),
                         "missing or too many equal operator")
        with self.assertRaises(ValueError) as cm:
            split_expression("5 * = X^0 + 4 = * X = ^1")
        self.assertEqual(str(cm.exception),
                         "missing or too many equal operator")

    def test_empty_left_expression(self):
        with self.assertRaises(ValueError) as cm:
            split_expression("   = 5 * X^0 + 4 * X^1")
        self.assertEqual(str(cm.exception), "expression is not complete")

    #
    # check_term_pattern(terms: list[str]) -> bool
    #
    def test_check_term_pattern(self):
        self.assertEqual(check_term_pattern(['+5*X^0', '+4*X^1']), True)
        self.assertEqual(check_term_pattern(['+5*X', '+4*X^1']), False)
        self.assertEqual(check_term_pattern(['+5*X  ^ 334', '+4*X^1']), False)
        self.assertEqual(check_term_pattern(['+5*X^334', '+4*X^1']), True)
        self.assertEqual(check_term_pattern(
            ['+5*X^0', '+4*X^1', '-9.3*X^2']), True)
        self.assertEqual(check_term_pattern(['+1*X^0']), True)


class TestSolve(ut.TestCase):
    def test_quadratic_equations(self):
        self.assertEqual(solve_quadratic_equation(
            [[7.0], [-2.0], [3.0]]), "Discriminant is strictly negative, the two solutions are:\n0.333333 + 1.490712i\n0.333333 - 1.490712i")
        self.assertEqual(solve_quadratic_equation([[4.0], [
                         4.0], [-9.3]]), "Discriminant is strictly positive, the two solutions are:\n0.905239\n-0.475131")


if __name__ == "__main__":
    ut.main()

#  with self.assertRaises(AssertionError) as cm:
    # Stark("Ned", 123)
    # self.assertEqual(str(cm.exception), 'is_alive must be bool')
