from .. import cli


def main():
    print('Welcome to the Brain Games!')
    user = cli.welcome_user()
    if cli.loop():
        print(f'Congratulations, {user}!')
    else:
        print(f'Let\'s try again, {user}!')


if __name__ == '__main__':
    main()
