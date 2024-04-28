from brain_games.core.base_game import base_game
from brain_games.core.tools import ask_about_even, validate_input


def even_quiz():
    base_game("Answer \"yes\" if the number is even, "
              "otherwise answer \"no\".", ask_about_even,
              validate_input)
