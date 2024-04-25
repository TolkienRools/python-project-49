from brain_games.core.base_game import base_game
from brain_games.core.tools import ask_about_gcd, validate_input


def gcd_quiz():
    base_game("Find the greatest common divisor "
              "of given numbers. ", ask_about_gcd,
              validate_input)
