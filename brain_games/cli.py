import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello,', name)
    return name.strip()


def question(q: str, q_prompt: str):
    print(q)
    answer = prompt.string(q_prompt)
    return answer.strip()
