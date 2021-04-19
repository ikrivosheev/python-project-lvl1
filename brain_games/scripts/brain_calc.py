from .. import engine
from ..games import calc


def main():
    engine.game(calc.HEADER, calc.game_step)


if __name__ == '__main__':
    main()
