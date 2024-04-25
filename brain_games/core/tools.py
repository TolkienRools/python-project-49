import random
import prompt


def generate_number():
    return random.randint(0, 100)


def is_even(number):
    return 'yes' if number % 2 == 0 else 'no'


def ask_about_even():
    question = generate_number()
    return question, is_even(question)


def validate_input(message):
    return prompt.string(message)


def calc_result(first_num, second_num, sign):
    match sign:
        case "+":
            return first_num + second_num
        case "-":
            return first_num - second_num
        case "*":
            return first_num * second_num


def ask_about_calc():
    sign = random.choice(['+', '-', '*'])

    first_number, second_number = generate_number(), generate_number()
    return (f"{first_number} {sign} {second_number}",
            str(calc_result(first_number, second_number, sign)))


def find_gcd(first_num, second_num):
    if second_num == 0:
        return first_num
    else:
        return find_gcd(second_num, first_num % second_num)


def ask_about_gcd():

    first_number, second_number = generate_number(), generate_number()
    return (f"{first_number} {second_number}",
            str(find_gcd(first_number, second_number)))
