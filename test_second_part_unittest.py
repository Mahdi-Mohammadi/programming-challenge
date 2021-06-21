import os
import yaml
import random
import unittest
from second_part import is_alpha
from second_part import is_int
from second_part import is_float
from second_part import type_detector


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


class TestTypeDetector(unittest.TestCase):
    test_cases = [
        dict(input_string='AAA', result='alphabetical strings'),
        dict(input_string='AAA1', result='alphanumeric'),
        dict(input_string=' A1A1A ', result='alphanumeric'),
        dict(input_string='1', result='integer'),
        dict(input_string='11', result='integer'),
        dict(input_string='1.1', result='real numbers'),
        dict(input_string='111111.1', result='real numbers'),
        dict(input_string='1.111111', result='real numbers'),
    ]

    def test_detection(self):
        for case in self.test_cases:
            self.assertEqual(type_detector(case['input_string']), case['result'])


if __name__ == '__main__':
    unittest.main()
