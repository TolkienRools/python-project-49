from brain_games.core.base_game import base_game
from brain_games.core.tools import validate_input, generate_number

EVEN_QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def ask_about_even():
    question = generate_number()
    true_answer = 'yes' if is_even(question) else 'no'
    return question, true_answer


def even_quiz():
    base_game(EVEN_QUESTION, ask_about_even, validate_input)
