import os
import random
import string
import yaml


def get_alpha(min_length: int = 1, max_length: int = 10) -> str:
    return ''.join([random.choice(string.ascii_lowercase) for _ in range(random.randint(min_length, max_length))])


def get_alphanumeric(min_length: int = 2, max_length: int = 10) -> str:
    alphanumeric = ''.join([random.choice(string.ascii_lowercase + string.digits) for _ in
                            range(random.randint(min_length, max_length))])
    if not any(map(str.isdigit, alphanumeric)):
        alphanumeric = get_alphanumeric(min_length, max_length)
    if not any(map(str.isalpha, alphanumeric)):
        alphanumeric = get_alphanumeric(min_length, max_length)
    return alphanumeric


def get_space(input_string: str, min_length, max_length):
    before_space_length = random.randint(min_length, max_length - 1)
    after_space_length = random.randint(1, max_length - before_space_length)
    return ' ' * before_space_length + input_string + ' ' * after_space_length


def get_int(min_length: int = 1, max_length: int = 10) -> str:
    return str(random.randint(10 ** (min_length - 1), 10 ** (max_length - 1)))


def get_float(min_length: int = 1, max_length: int = 10) -> str:
    float_length = random.randint(min_length, max_length)
    rand_float = round(random.uniform(10 ** min_length, 10 ** max_length / 2), float_length)
    return str(rand_float)[-max_length:]


def create_random_file(file_path: str, max_file_size: int, length_config: dict) -> bool:
    random_types = ['alpha', 'alphanumeric', 'int', 'float']
    file_size = 0
    min_length = length_config['min']
    max_length = length_config['max']
    min_space = length_config['min_space']
    max_space = length_config['max_space']
    with open(file_path, 'a') as file:
        while file_size < max_file_size:
            rand_type = random.choice(random_types)
            if rand_type == 'alpha':
                output = get_alpha(min_length, max_length)
            elif rand_type == 'alphanumeric':
                output = get_space(get_alphanumeric(min_length, max_length), min_space, max_space)
            elif rand_type == 'int':
                output = get_int(min_length, max_length)
            elif rand_type == 'float':
                output = get_float(min_length, max_length)
            file.write(output + ', ')
            file.tell()
            file_size = os.stat(file_path).st_size
        if file_size > max_file_size:
            with open(file_path, 'rb+') as file_byte:
                file_byte.seek(-(file_size - max_file_size), os.SEEK_END)
                file_byte.truncate()
        file.close()
    return True


if __name__ == '__main__':
    config = yaml.safe_load(open("config.yml"))
    file_path = config['result']['path']
    if os.path.exists(file_path):
        os.remove(file_path)
    create_random_file(file_path, config['result']['size'], dict(config['length'].items()))
