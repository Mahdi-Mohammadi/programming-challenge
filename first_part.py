import random
import string


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
