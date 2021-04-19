import random

from .utils import get_gcd
from .utils import is_prime


def is_even(start_q: int = 0, end_q: int = 100):
    q = random.randint(start_q, end_q)
    return f'Question: {q}', 'yes' if (q % 2) == 0 else 'no'


def calc(start: int = 0, end: int = 20):
    operations = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b
    }
    a = random.randint(start, end)
    b = random.randint(start, end)
    op = random.choice(list(operations.keys()))
    expected_result = operations[op](a, b)

    return f'Question: {a} {op} {b}', str(expected_result)


def gcd(start: int = 1, end: int = 30):
    a = random.randint(start, end)
    b = random.randint(start, end)
    q = f'Question: {a} {b}'
    return q, str(get_gcd(a, b))


def progression(
    start_size: int = 5,
    end_size: int = 10,
    start_step: int = 1,
    end_step: int = 20,
    start_first: int = 0,
    end_first: int = 30,
):
    size = random.randint(start_size, end_size)
    step = random.randint(start_step, end_step)
    first = random.randint(start_first, end_first)
    hidden_position = random.randint(0, size - 1)

    elements = []
    elem = first
    for i in range(size):
        if i == hidden_position:
            elements.append('..')
        else:
            elements.append(str(elem))
        elem += step

    hidden_elem = first + hidden_position * step
    return f'Question: {" ".join(elements)}', str(hidden_elem)


def prime(start: int = 1, end: int = 30):
    value = random.randint(start, end)
    return f'Question: {value}', 'yes' if is_prime(value) else 'no'
