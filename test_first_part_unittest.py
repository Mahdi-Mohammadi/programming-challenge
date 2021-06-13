import unittest
import random
from first_part import get_alpha
from first_part import get_alphanumeric
from first_part import get_space


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
        output_len = random.randint(2, 20)
        self.assertIsInstance(get_alphanumeric(output_len, output_len), str, f"Output should be {str}")

    def test_length(self):
        output_len = random.randint(2, 20)
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


class TestSpace(unittest.TestCase):
    def test_output_type(self):
        output_len = random.randint(2, 20)
        self.assertIsInstance(get_space('A', 2, output_len), str, f"Output should be {str}")

    def test_random_length(self):
        output_len = random.randint(10, 20)
        self.assertTrue(3 <= len(get_space('A', 2, output_len)) <= output_len + 1,
                        f"Length should be random and between 3 and {output_len + 1}")

    def test_before_space_exist(self):
        self.assertTrue(get_space('A', 2, 20)[0] == ' ', "First char must be space")

    def test_after_space_exist(self):
        self.assertTrue(get_space('A', 2, 20)[-1] == ' ', "Last char must be space")


if __name__ == '__main__':
    unittest.main()
