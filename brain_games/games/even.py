import random


HEADER = 'Answer "yes" if the number is even, otherwise answer "no".'


def prepare_round_data(start: int = 0, end: int = 100):
    number = random.randint(start, end)
    correct_answer = 'yes' if (number % 2) == 0 else 'no'
    return f'{number}', correct_answer
