#!/usr/bin/env python3
from brain_games.core.base_game import play_base_game
from brain_games.games import gcd_game


def main():
    play_base_game(gcd_game)


if __name__ == '__main__':
    main()
