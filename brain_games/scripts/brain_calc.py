#!/usr/bin/env python3
"""Brain Calc"""
from .. import engine
from ..games import CALC_GAME


def main():
    """Brain Calc game"""
    engine.game(*CALC_GAME)


if __name__ == '__main__':
    main()
