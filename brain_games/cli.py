import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello,', name)
    return name.strip()


def request_user(question: str, q_prompt: str):
    print(question)
    answer = prompt.string(q_prompt)
    return answer.strip()
