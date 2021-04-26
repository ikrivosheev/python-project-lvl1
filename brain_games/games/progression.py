import random
import typing as t

HEADER = 'Find the greatest common divisor of given numbers.'


def prepare_round_data(
    size_range: t.Tuple[int, int] = (5, 10),
    step_range: t.Tuple[int, int] = (1, 20),
    first_range: t.Tuple[int, int] = (0, 30),
):
    size = random.randint(*size_range)
    step = random.randint(*step_range)
    first = random.randint(*first_range)
    hidden_position = random.randint(0, size - 1)

    question = []
    elem = first
    for i in range(size):
        if i == hidden_position:
            question.append('..')
        else:
            question.append(str(elem))
        elem += step

    hidden_elem = first + hidden_position * step
    return f'{" ".join(question)}', f'{hidden_elem}'
