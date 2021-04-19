import random

import prompt

from .cli import bool_question


def _is_even(start_q: int = 0, end_q: int = 100):
    q = random.randint(start_q, end_q)

    is_even = (q % 2) == 0
    print('Question: ', q)
    try:
        answer = bool_question('Your answer: ')
    except ValueError:
        print('Inccorect answer')
        return False

    if answer and not is_even:
        print('\'yes\' is wrong answer ;(. Correct answer was \'no\'.')
        return False
    elif not answer and is_even:
        print('\'no\' is wrong answer ;(. Correct answer was \'yes\'')
        return False

    print('Correct!')
    return True


def _calc(start: int = 0, end: int = 20):
    a = random.randint(start, end)
    b = random.randint(start, end)
    op = random.choice(['+', '-', '*'])

    if op == '+':
        expected_result = a + b
    elif op == '-':
        expected_result = a - b
    else:
        expected_result = a * b

    print(f'Question: {a} {op} {b}')
    answer = prompt.integer(prompt='Your answer: ')

    if answer != expected_result:
        print(f'\'{answer}\' is wrong answer ;(. '
              f'Correct answer was \' {expected_result}\'')
        return False

    print('Correct!')
    return True


def _loop(hello_str: str, one_step, attempts: int = 3) -> bool:
    print(hello_str)

    for i in range(attempts):
        if not one_step():
            return False

    return True


def is_even(user):
    result = _loop(
        'Answer "yes" if the number is even, otherwise answer "no".',
        _is_even,
    )
    if result:
        print(f'Congratulations, {user}!')
    else:
        print(f'Let\'s try again, {user}!')


def calc(user):
    result = _loop(
        'What is the result of the expression?',
        _calc,
    )
    if result:
        print(f'Congratulations, {user}!')
    else:
        print(f'Let\'s try again, {user}!')
