from brain_games.core.base_game import base_game
from brain_games.core.tools import ask_about_calc, validate_input


def calc_quiz():
    base_game("What is the result of the expression?",
              ask_about_calc, validate_input)
