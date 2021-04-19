from .. import games
from .. import engine


def main():
    engine.game(
        'Find the greatest common divisor of given numbers.',
        games.gcd
    )


if __name__ == '__main__':
    main()
