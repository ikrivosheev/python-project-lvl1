import random


HEADER = 'Answer "yes" if the number is even, otherwise answer "no".'


def play(start: int = 0, end: int = 100):
    q = random.randint(start, end)
    return f'{q}', 'yes' if (q % 2) == 0 else 'no'
