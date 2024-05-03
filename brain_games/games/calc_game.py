from brain_games.core.base_game import base_game
from brain_games.core.tools import validate_input, generate_number
import random

CALC_QUESTION = 'What is the result of the expression?'


def calc_result(first_num, second_num, sign):
    match sign:
        case '+':
            return first_num + second_num
        case '-':
            return first_num - second_num
        case '*':
            return first_num * second_num


def ask_about_calc():
    sign = random.choice(['+', '-', '*'])

    first_number, second_number = generate_number(), generate_number()
    return (f'{first_number} {sign} {second_number}',
            str(calc_result(first_number, second_number, sign)))


def calc_quiz():
    base_game(CALC_QUESTION, ask_about_calc, validate_input)
