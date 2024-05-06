#!/usr/bin/env python3
from brain_games.core.base_game import play_base_game
from brain_games.games.gcd_game import ask_about_gcd

GCD_QUESTION = 'Find the greatest common divisor of given numbers.'


def main():
    play_base_game(GCD_QUESTION, ask_about_gcd)


if __name__ == '__main__':
    main()
