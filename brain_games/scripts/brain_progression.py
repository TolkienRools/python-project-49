#!/usr/bin/env python3
from brain_games.core.base_game import play_base_game
from brain_games.games.progression_game import ask_about_progression

PROGRESSION_QUESTION = 'What number is missing in the progression?'


def main():
    play_base_game(PROGRESSION_QUESTION, ask_about_progression)


if __name__ == '__main__':
    main()
