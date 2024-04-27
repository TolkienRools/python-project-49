from brain_games.core.base_game import base_game
from brain_games.core.tools import ask_about_prime, validate_input


def prime_quiz():
    base_game("Answer \"yes\" if given number is prime. "
              "Otherwise answer \"no\".", ask_about_prime,
              validate_input)
