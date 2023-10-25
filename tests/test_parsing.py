
import unittest as ut
import sys
import os

from src.parsing_utils import split_expression


class TestParsing(ut.TestCase):
    def test_split_expression(self):
        self.assertEqual(split_expression(
            "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"), ("5*X^0+4*X^1-9 .3*X^2", "1*X^0"))
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


if __name__ == "__main__":
    ut.main()

#  with self.assertRaises(AssertionError) as cm:
    # Stark("Ned", 123)
    # self.assertEqual(str(cm.exception), 'is_alive must be bool')
