import random

HEADER = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number: int) -> bool:
    if number % 2 == 0:
        return number == 2

    divider = 3
    divider_square = divider ** 2
    while divider_square <= number and number % divider != 0:
        divider += 2
        divider_square = divider ** 2
    return divider_square > number


def prepare_round_data(start: int = 1, end: int = 30):
    value = random.randint(start, end)
    correct_answer = 'yes' if is_prime(value) else 'no'
    return f'{value}', correct_answer
