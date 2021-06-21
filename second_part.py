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


def format_output(input_string: str, input_type: str) -> str:
    return f"{input_string} - {input_type}"


def file_type_detector(source_file_path: str, output_file_path: str) -> None:
    output_file = open(output_file_path, 'w')
    with open(source_file_path, 'r') as source_file:
        terms = source_file.read().split(',')
        for term in terms:
            term = term.strip()
            if not term:
                continue
            result = format_output(term, type_detector(term))
            print(result)
            output_file.write(result + '\n')
        output_file.close()


if __name__ == '__main__':
    config = yaml.safe_load(open("config.yml"))
    source_file_path = config['result']['path']
    if not os.path.exists(source_file_path):
        raise FileExistsError(f"File '{source_file_path}' does not exist")
    file_type_detector(source_file_path, config['result']['detected_path'])
