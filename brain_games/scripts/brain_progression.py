#!/usr/bin/env python3
from brain_games.core.base_game import play_base_game
from brain_games.games import progression_game


def main():
    play_base_game(progression_game)


if __name__ == '__main__':
    main()
