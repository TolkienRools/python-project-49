import random

GAME_QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_CHECK_EVEN_NUMBER = 0
MAX_CHECK_EVEN_NUMBER = 100


def is_even(number):
    return number % 2 == 0


def question_func():
    question = random.randint(MIN_CHECK_EVEN_NUMBER, MAX_CHECK_EVEN_NUMBER)
    true_answer = 'yes' if is_even(question) else 'no'
    return question, true_answer
