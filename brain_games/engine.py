from .cli import request_user
from .cli import welcome_user


def _loop(prepare_round_data, attempts: int = 3, **kwargs) -> bool:
    for i in range(attempts):
        question, correct_answer = prepare_round_data(**kwargs)
        answer = request_user(f'Question: {question}', 'Your answer: ')
        if answer != correct_answer:
            print(f'\'{answer}\' is wrong answer ;(. '
                  f'Correct answer was \'{correct_answer}\'.')
            return False
        print('Correct!')
    return True


def run(game, attempts: int = 3, **kwargs):
    print('Welcome to the Brain Games!')
    user = welcome_user()

    print(game.HEADER)
    if _loop(game.prepare_round_data, attempts, **kwargs):
        print(f'Congratulations, {user}!')
    else:
        print(f'Let\'s try again, {user}!')
