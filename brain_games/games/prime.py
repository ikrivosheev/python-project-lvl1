import random

from ..utils import is_prime

HEADER = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_step(start: int = 1, end: int = 30):
    value = random.randint(start, end)
    return f'Question: {value}', 'yes' if is_prime(value) else 'no'
