import unittest
import random
from first_part import get_alpha
from first_part import get_alphanumeric


class TestAlpha(unittest.TestCase):
    def test_output_type(self):
        output_len = random.randint(1, 20)
        self.assertIsInstance(get_alpha(output_len, output_len), str, f"Output should be {str}")

    def test_length(self):
        output_len = random.randint(1, 20)
        self.assertEqual(len(get_alpha(output_len, output_len)), output_len, f"Length should be {output_len}")

    def test_random_length(self):
        output_len = random.randint(10, 20)
        self.assertTrue(1 <= len(get_alpha(1, output_len)) <= output_len,
                        f"Length should be random and between 1 and {output_len}")

    def test_is_alpha(self):
        self.assertTrue(get_alpha(100, 100).isalpha(), "Output should be contains alpha")


class TestAlphanumeric(unittest.TestCase):
    def test_output_type(self):
        output_len = random.randint(1, 20)
        self.assertIsInstance(get_alphanumeric(output_len, output_len), str, f"Output should be {str}")

    def test_length(self):
        output_len = random.randint(1, 20)
        self.assertEqual(len(get_alphanumeric(output_len, output_len)), output_len, f"Length should be {output_len}")

    def test_random_length(self):
        output_len = random.randint(10, 20)
        self.assertTrue(1 <= len(get_alphanumeric(1, output_len)) <= output_len,
                        f"Length should be random and between 1 and {output_len}")

    def test_alpha_exist(self):
        self.assertTrue(any(map(str.isalpha, get_alphanumeric(2, 2))),
                        "Output should be contains at least one alphabetical char")

    def test_digit_exist(self):
        self.assertTrue(any(map(str.isdigit, get_alphanumeric(2, 2))),
                        "Output should be contains at least one digit char")


if __name__ == '__main__':
    unittest.main()
