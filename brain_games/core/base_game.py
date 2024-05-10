import prompt

QUESTIONS_COUNT = 3


def greeting():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I gave your name? ')
    print(f'Hello, {name}!')
    return name


def play_base_game(game_module):

    user_name = greeting()
    print(game_module.GAME_QUESTION)

    for _ in range(QUESTIONS_COUNT):
        question, true_answer = game_module.question_func()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer != true_answer:
            print(f'\'{user_answer}\' is wrong answer'
                  f' ;(. Correct answer was \'{true_answer}\'.')
            print(f'Let\'s try again, {user_name}!')
            break
        else:
            print('Correct!')
    else:
        print(f'Congratulations, {user_name}!')
