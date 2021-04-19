import random
import typing as t


HEADER = 'Find the greatest common divisor of given numbers.'


def game_step(
    size_range: t.Tuple[int, int] = (5, 10),
    step_range: t.Tuple[int, int] = (1, 20),
    first_range: t.Tuple[int, int] = (0, 30),
):
    size = random.randint(*size_range)
    step = random.randint(*step_range)
    first = random.randint(*first_range)
    hidden_position = random.randint(0, size - 1)

    elements = []
    elem = first
    for i in range(size):
        if i == hidden_position:
            elements.append('..')
        else:
            elements.append(str(elem))
        elem += step

    hidden_elem = first + hidden_position * step
    return f'Question: {" ".join(elements)}', str(hidden_elem)
