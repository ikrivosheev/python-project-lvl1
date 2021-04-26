import random

HEADER = 'Find the greatest common divisor of given numbers.'


def get_gcd(a: int, b: int):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


def prepare_round_data(start: int = 1, end: int = 30):
    a = random.randint(start, end)
    b = random.randint(start, end)
    gcd = get_gcd(a, b)
    return f'{a} {b}', f'{gcd}'
