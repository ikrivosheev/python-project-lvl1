from .. import games
from .. import engine


def main():
    engine.game(
        'Answer "yes" if the number is even, otherwise answer "no".',
        games.is_even,
    )


if __name__ == '__main__':
    main()
