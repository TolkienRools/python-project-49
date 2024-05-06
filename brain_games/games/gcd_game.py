from math import gcd
import random

MIN_OPERAND_VALUE = 0
MAX_OPERAND_VALUE = 100


def ask_about_gcd():

    first_number = random.randint(MIN_OPERAND_VALUE, MAX_OPERAND_VALUE)
    second_number = random.randint(MIN_OPERAND_VALUE, MAX_OPERAND_VALUE)
    return (f'{first_number} {second_number}',
            str(gcd(first_number, second_number)))
