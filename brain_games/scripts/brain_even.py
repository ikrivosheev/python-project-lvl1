from .. import engine
from ..games import even


def main():
    engine.game(even.HEADER, even.game_step)


if __name__ == '__main__':
    main()
