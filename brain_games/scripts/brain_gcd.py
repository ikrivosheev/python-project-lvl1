from .. import engine
from ..games import gcd


def main():
    engine.game(gcd.HEADER, gcd.game_step)


if __name__ == '__main__':
    main()
