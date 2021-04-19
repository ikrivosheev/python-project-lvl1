import random

HEADER = 'What is the result of the expression?'
OPERATIONS = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b
}


def game_step(start: int = 0, end: int = 20):
    a = random.randint(start, end)
    b = random.randint(start, end)
    op = random.choice(list(OPERATIONS.keys()))
    expected_result = OPERATIONS[op](a, b)

    return f'Question: {a} {op} {b}', str(expected_result)
