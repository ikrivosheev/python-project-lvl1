import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello, ', name)
    return name.strip()


def question(q: str):
    print(q)
    answer = prompt.string('Your answer: ')
    return answer.strip()
