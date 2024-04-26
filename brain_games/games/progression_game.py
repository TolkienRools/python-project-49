from brain_games.core.base_game import base_game
from brain_games.core.tools import ask_about_progression, validate_input


def progression_quiz():
    base_game("What number is missing in the progression?",
              ask_about_progression,
              validate_input)
