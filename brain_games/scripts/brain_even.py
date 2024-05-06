#!/usr/bin/env python3
from brain_games.core.base_game import play_base_game
from brain_games.games.even_game import ask_about_even

EVEN_QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def main():
    play_base_game(EVEN_QUESTION, ask_about_even)


if __name__ == '__main__':
    main()
