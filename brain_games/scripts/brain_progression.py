from .. import engine
from ..games import progression


def main():
    engine.game(progression.HEADER, progression.game_step)


if __name__ == '__main__':
    main()
