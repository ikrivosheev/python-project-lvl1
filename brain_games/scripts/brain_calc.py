from .. import games
from .. import engine


def main():
    engine.game('What is the result of the expression?', games.calc)


if __name__ == '__main__':
    main()
