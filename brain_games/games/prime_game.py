import random

GAME_QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_CHECK_PRIME_NUMBER = 0
MAX_CHECK_PRIME_NUMBER = 100


def is_prime(number):
    if number in (0, 1):
        return False
    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def question_func():
    number_to_check = random.randint(MIN_CHECK_PRIME_NUMBER,
                                     MAX_CHECK_PRIME_NUMBER)
    true_answer = 'yes' if is_prime(number_to_check) else 'no'
    return str(number_to_check), true_answer
