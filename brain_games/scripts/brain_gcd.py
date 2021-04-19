#!/usr/bin/env python3
"""Brain GCD"""
from .. import engine
from ..games import GCD_GAME


def main():
    engine.game(*GCD_GAME)


if __name__ == '__main__':
    main()
