from brain_games.core.base_game import base_game
from brain_games.core.tools import validate_input, generate_number
from math import gcd

GCD_QUESTION = 'Find the greatest common divisor of given numbers.'


def ask_about_gcd():

    first_number, second_number = generate_number(), generate_number()
    return (f'{first_number} {second_number}',
            str(gcd(first_number, second_number)))


def gcd_quiz():
    base_game(GCD_QUESTION, ask_about_gcd, validate_input)
