from brain_games.core.base_game import base_game
from brain_games.core.tools import validate_input
import random

PRIME_QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def ask_about_prime():
    number_to_check = random.randint(1, 100)
    true_answer = 'yes' if is_prime(number_to_check) else 'no'
    return str(number_to_check), true_answer


def prime_quiz():
    base_game(PRIME_QUESTION, ask_about_prime, validate_input)
