#!/usr/bin/env python3
from brain_games.core.base_game import play_base_game
from brain_games.games.calc_game import ask_about_calc

CALC_QUESTION = 'What is the result of the expression?'


def main():
    play_base_game(CALC_QUESTION, ask_about_calc)


if __name__ == '__main__':
    main()
