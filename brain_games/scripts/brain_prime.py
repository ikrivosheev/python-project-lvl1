#!/usr/bin/env python3
"""Brain Prime"""
from .. import engine
from ..games import PRIME_GAME


def main():
    engine.game(*PRIME_GAME)


if __name__ == '__main__':
    main()
