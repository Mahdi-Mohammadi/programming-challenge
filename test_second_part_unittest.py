import os
import yaml
import random
import unittest
from second_part import is_alpha
from second_part import is_int
from second_part import is_float
from second_part import check_random_file


class TestAlpha(unittest.TestCase):
    true_test_cases = ['AA', 'aa', 'Aa']
    false_test_cases = ['AA1', '1AA', '1', '1.1', 'a.a', 'Aa@']

    def test_true_cases(self):
        for true_case in self.true_test_cases:
            self.assertTrue(is_alpha(true_case))

    def test_false_cases(self):
        for false_case in self.false_test_cases:
            self.assertFalse(is_alpha(false_case))


class TestInt(unittest.TestCase):
    true_test_cases = ['1', '11', '111']
    false_test_cases = ['AA', '11.1', '0.1', 'a.a', 'Aa@']

    def test_true_cases(self):
        for true_case in self.true_test_cases:
            self.assertTrue(is_int(true_case), true_case)

    def test_false_cases(self):
        for false_case in self.false_test_cases:
            self.assertFalse(is_int(false_case), false_case)


class TestFloat(unittest.TestCase):
    true_test_cases = ['1.0', '11.1', '111.123456789']
    false_test_cases = ['AA', '11', '0.', 'a.a', 'Aa@']

    def test_true_cases(self):
        for true_case in self.true_test_cases:
            self.assertTrue(is_float(true_case), true_case)

    def test_false_cases(self):
        for false_case in self.false_test_cases:
            self.assertFalse(is_float(false_case), false_case)


if __name__ == '__main__':
    unittest.main()
