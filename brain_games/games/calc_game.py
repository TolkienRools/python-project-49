import random

MIN_OPERAND_VALUE = 0
MAX_OPERAND_VALUE = 100


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

    first_number = random.randint(MIN_OPERAND_VALUE, MAX_OPERAND_VALUE)
    second_number = random.randint(MIN_OPERAND_VALUE, MAX_OPERAND_VALUE)
    return (f'{first_number} {sign} {second_number}',
            str(calc_result(first_number, second_number, sign)))
