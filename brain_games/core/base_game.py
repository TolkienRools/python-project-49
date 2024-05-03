import prompt

NUMBER_OF_QUESTION = 3


def greeting():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I gave your name? ')
    print(f'Hello, {name}!')
    return name


def base_game(main_question,
              question_func,
              validate_user_answer):

    user_name = greeting()
    print(main_question)

    for _ in range(NUMBER_OF_QUESTION):
        question, true_answer = question_func()
        print(f'Question: {question}')
        user_answer = validate_user_answer('Your answer: ')
        if user_answer != true_answer:
            print(f'\'{user_answer}\' is wrong answer'
                  f' ;(. Correct answer was \'{true_answer}\'.')
            print(f'Let\'s try again, {user_name}!')
            break
        else:
            print('Correct!')
    else:
        print(f'Congratulations, {user_name}!')
