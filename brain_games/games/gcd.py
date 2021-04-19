import random

from ..utils import get_gcd

HEADER = 'Find the greatest common divisor of given numbers.',


def game_step(start: int = 1, end: int = 30):
    a = random.randint(start, end)
    b = random.randint(start, end)
    q = f'Question: {a} {b}'
    return q, str(get_gcd(a, b))
