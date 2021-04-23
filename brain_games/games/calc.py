import random
import operator

HEADER = 'What is the result of the expression?'
OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}


def play(start: int = 0, end: int = 20):
    a = random.randint(start, end)
    b = random.randint(start, end)
    op = random.choice(list(OPERATIONS.keys()))
    expected_result = OPERATIONS[op](a, b)

    return f'{a} {op} {b}', str(expected_result)
