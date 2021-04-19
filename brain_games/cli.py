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
