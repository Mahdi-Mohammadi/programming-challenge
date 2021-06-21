import os
import yaml
import unittest

from first_part import create_random_file
from second_part import file_type_detector


class TestIntegration(unittest.TestCase):
    file_path = 'test_file.txt'
    result_file_path = 'result_test_file.txt'
    file_size = 10 * 100
    length = dict(min=2, max=10, min_space=2, max_space=10)

    def remove_file(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        if os.path.exists(self.result_file_path):
            os.remove(self.result_file_path)

    def setUp(self):
        with open("../test_config.yml") as config_file:
            config = yaml.safe_load(config_file)
            self.file_path = config['result']['path']
            self.result_file_path = config['result']['detected_path']
            self.file_size = config['result']['size']
            self.length = dict(config['length'].items())
        self.remove_file()

    def tearDown(self) -> None:
        self.remove_file()

    def test_result(self):
        create_random_file(self.file_path, self.file_size, self.length)
        with open(self.file_path) as source_file:
            terms = source_file.read().split(',')
            total_term = len([term for term in terms if term.strip()])

        file_type_detector(self.file_path, self.result_file_path)
        with open(self.result_file_path) as result_file:
            total_result_term = len(result_file.readlines())

        self.assertEqual(total_term, total_result_term, "Total terms in source is not equal to total result")


if __name__ == '__main__':
    unittest.main()
