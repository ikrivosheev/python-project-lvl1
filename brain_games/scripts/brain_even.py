from .. import cli
from .. import games


def main():
    print('Welcome to the Brain Games!')
    user = cli.welcome_user()
    games.is_even(user)


if __name__ == '__main__':
    main()
