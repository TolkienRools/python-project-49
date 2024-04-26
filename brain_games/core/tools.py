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


def generate_progression():
    start = random.randint(0, 30)
    step = random.randint(1, 10)
    terms = random.randint(5, 10)
    progression = []
    for i in range(1, terms + 1):
        term_n = start + (i - 1) * step
        progression.append(term_n)

    return progression, terms


def ask_about_progression():
    progression, terms = generate_progression()
    stringified_progression = list(map(str, progression))
    index_pass_term = random.randint(0, terms-1)
    pass_term = stringified_progression[index_pass_term]
    stringified_progression[index_pass_term] = '..'

    return " ".join(stringified_progression), pass_term


