from .. import games
from .. import engine


def main():
    engine.game(
        'Answer "yes" if given number is prime. Otherwise answer "no".',
        games.prime
    )


if __name__ == '__main__':
    main()
