from math import gcd
import random

GAME_QUESTION = 'Find the greatest common divisor of given numbers.'
MIN_OPERAND_VALUE = 0
MAX_OPERAND_VALUE = 100


def question_func():

    first_number = random.randint(MIN_OPERAND_VALUE, MAX_OPERAND_VALUE)
    second_number = random.randint(MIN_OPERAND_VALUE, MAX_OPERAND_VALUE)
    return (f'{first_number} {second_number}',
            str(gcd(first_number, second_number)))
