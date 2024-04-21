import prompt
import random


def greeting():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name! ")
    print(f"Hello, {name}!")
    return name


def is_even(number):
    return 'yes' if number % 2 == 0 else 'no'


def even_quiz(user_name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):
        number = random.randint(0, 100)
        print(f"Question: {number}")
        correct_answer = is_even(number)
        answer = prompt.string("Your answer: ")
        if answer == correct_answer:
            print("Correct!")
            continue
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was '{correct_answer}'")
            print(f"Let's try again, {user_name}!")
            return

    print(f"Congratulations, {user_name}!")
    return

