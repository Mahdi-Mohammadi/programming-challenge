import os
import yaml


def is_alpha(input_string: str) -> bool:
    return input_string.isalpha()



def is_int(input_string: str) -> bool:
    return input_string.isnumeric()


def is_float(input_string: str) -> bool:
    pass


def check_random_file(file_path: str) -> bool:
    pass


if __name__ == '__main__':
    config = yaml.safe_load(open("config.yml"))
    file_path = config['result']['path']
    if not os.path.exists(file_path):
        raise FileExistsError(f"File '{file_path}' does not exist")
    check_random_file(file_path)
