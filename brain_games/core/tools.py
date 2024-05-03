import random
import prompt


def generate_number():
    return random.randint(0, 100)


def validate_input(message):
    return prompt.string(message)
