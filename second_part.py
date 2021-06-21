import os
import yaml


def is_alpha(input_string: str) -> bool:
    return input_string.isalpha()


def is_int(input_string: str) -> bool:
    return input_string.isdigit()


def is_float(input_string: str) -> bool:
    if '.' not in input_string:
        return False
    num = input_string.split('.')
    if num[-1] is not None and num[-1].isdigit():
        return True
    return False


def type_detector(input_string: str) -> str:
    if is_float(input_string):
        return 'real numbers'
    elif is_int(input_string) and not is_alpha(input_string):
        return 'integer'
    elif not is_alpha(input_string):
        return 'alphanumeric'
    else:
        return 'alphabetical strings'


def print_output(input_string: str, input_type: str) -> None:
    print(f"{input_string} - {input_type}")


def file_type_detector(file_path: str) -> None:
    with open(file_path, 'r') as file:
        items = file.read().split(',')
        for item in items:
            item = item.strip()
            print_output(item, type_detector(item))


if __name__ == '__main__':
    config = yaml.safe_load(open("config.yml"))
    file_path = config['result']['path']
    if not os.path.exists(file_path):
        raise FileExistsError(f"File '{file_path}' does not exist")
    file_type_detector(file_path)
