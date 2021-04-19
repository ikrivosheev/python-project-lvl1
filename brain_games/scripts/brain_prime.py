from .. import engine
from ..games import prime


def main():
    engine.game(prime.HEADER, prime.game_step)


if __name__ == '__main__':
    main()
