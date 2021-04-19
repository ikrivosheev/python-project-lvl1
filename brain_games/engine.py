from .cli import question
from .cli import welcome_user


def _loop(game_step, attempts: int = 3, **kwargs) -> bool:
    for i in range(attempts):
        q, correct_answer = game_step(**kwargs)
        answer = question(q)
        if answer != correct_answer:
            print(f'\'{answer}\' is wrong answer ;(. '
                  f'Correct answer was \'{correct_answer}\'.')
            return False
        print('Correct!')
    return True


def game(description, game_step, attempts: int = 3, **kwargs):
    print('Welcome to the Brain Games!')
    user = welcome_user()

    print(description)
    if _loop(game_step, attempts, **kwargs):
        print(f'Congratulations, {user}!')
    else:
        print(f'Let\'s try again, {user}!')
