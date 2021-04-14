import random

import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello, ', name)
    return name.strip()


def bool_question(q, yes_answer='yes', no_answer='no'):
    answer = prompt.string(q)
    if answer == yes_answer:
        return True
    elif answer == no_answer:
        return False

    raise ValueError


def game_is_even(attempts: int = 3, start_q: int = 0, end_q: int = 100):
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for i in range(attempts):
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
