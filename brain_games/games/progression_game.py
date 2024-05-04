from brain_games.core.base_game import base_game
from brain_games.core.tools import validate_input
import random

PROGRESSION_QUESTION = 'What number is missing in the progression?'
MIN_FIRST_PROGRESSION_TERM = 0
MAX_FIRST_PROGRESSION_TERM = 30
MIN_PROGRESSION_STEP = 1
MAX_PROGRESSION_STEP = 10
MIN_TERMS_NUMBER = 5
MAX_TERMS_NUMBER = 10
MIN_PASS_TERM_INDEX = 0


def generate_progression():
    start = random.randint(MIN_FIRST_PROGRESSION_TERM,
                           MAX_FIRST_PROGRESSION_TERM)
    step = random.randint(MIN_PROGRESSION_STEP,
                          MAX_PROGRESSION_STEP)
    terms = random.randint(MIN_TERMS_NUMBER, MAX_TERMS_NUMBER)
    progression = []
    for i in range(1, terms + 1):
        term_n = start + (i - 1) * step
        progression.append(term_n)

    return progression, terms


def ask_about_progression():
    progression, terms = generate_progression()
    stringified_progression = list(map(str, progression))
    index_pass_term = random.randint(MIN_PASS_TERM_INDEX, terms - 1)
    pass_term = stringified_progression[index_pass_term]
    stringified_progression[index_pass_term] = '..'

    return ' '.join(stringified_progression), pass_term


def progression_quiz():
    base_game(PROGRESSION_QUESTION, ask_about_progression, validate_input)
