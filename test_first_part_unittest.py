import os
import yaml
import random
import unittest
from first_part import get_alpha
from first_part import get_alphanumeric
from first_part import get_space
from first_part import get_int
from first_part import get_float
from first_part import create_random_file


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
        output_len = random.randint(4, 20)
        self.assertIsInstance(get_space('A', 2, output_len), str, f"Output should be {str}")

    def test_random_length(self):
        output_len = random.randint(10, 20)
        self.assertTrue(3 <= len(get_space('A', 2, output_len)) <= output_len + 1,
                        f"Length should be random and between 3 and {output_len + 1}")

    def test_before_space_exist(self):
        self.assertTrue(get_space('A', 2, 20)[0] == ' ', "First char must be space")

    def test_after_space_exist(self):
        self.assertTrue(get_space('A', 2, 20)[-1] == ' ', "Last char must be space")


class TestInt(unittest.TestCase):
    def test_output_type(self):
        output_len = random.randint(1, 20)
        self.assertIsInstance(get_int(output_len, output_len), str, f"Output should be {str}")

    def test_length(self):
        output_len = random.randint(1, 20)
        self.assertEqual(len(get_int(output_len, output_len)), output_len, f"Length should be {output_len}")

    def test_random_length(self):
        output_len = random.randint(10, 20)
        self.assertTrue(1 <= len(get_int(1, output_len)) <= output_len,
                        f"Length should be random and between 1 and {output_len}")

    def test_alpha_exist(self):
        self.assertFalse(any(map(str.isalpha, get_int(20, 20))),
                         "Output should not be contains at least one alphabetical char")

    def test_digit(self):
        self.assertIsInstance(int(get_int(2, 2)), int, "Output should be digits")


class TestFloat(unittest.TestCase):
    def test_output_type(self):
        output_len = random.randint(3, 20)
        self.assertIsInstance(get_float(output_len, output_len), str, f"Output should be {str}")

    def test_length(self):
        output_len = random.randint(3, 20)
        self.assertEqual(len(get_float(output_len, output_len)), output_len, f"Length should be {output_len}")

    def test_random_length(self):
        output_len = random.randint(10, 20)
        self.assertTrue(1 <= len(get_float(3, output_len)) <= output_len,
                        f"Length should be random and between 1 and {output_len}")

    def test_point_exist(self):
        self.assertTrue('.' in get_float(20, 20), "Output should be contains point (.)")

    def test_float(self):
        self.assertIsInstance(float(get_float(4, 4)), float, "Output should be convert to float")


class TestCreateRandomFile(unittest.TestCase):
    file_path = 'test_file.txt'
    file_size = 10 * 100
    length = dict(min=2, max=10, min_space=2, max_space=10)

    def remove_file(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def setUp(self):
        with open("test_config.yml") as config_file:
            config = yaml.safe_load(config_file)
            self.file_path = config['result']['path']
            self.file_size = config['result']['size']
            self.length = dict(config['length'].items())
        self.remove_file()

    def tearDown(self) -> None:
        self.remove_file()

    def test_output_type(self):
        self.assertIsInstance(create_random_file(self.file_path, self.file_size, self.length), bool,
                              f"Output should be {bool}")

    def test_file_exist(self):
        create_random_file(self.file_path, self.file_size, self.length)
        self.assertTrue(os.path.exists(self.file_path), "Output file dose not exist")

    def test_file_size(self):
        create_random_file(self.file_path, self.file_size, self.length)
        self.assertEqual(os.stat(self.file_path).st_size, self.file_size, f"File size should be {self.file_size}")


if __name__ == '__main__':
    unittest.main()
