#!/usr/bin/env python3
from brain_games.core.base_game import play_base_game
from brain_games.games.prime_game import ask_about_prime

PRIME_QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():
    play_base_game(PRIME_QUESTION, ask_about_prime)


if __name__ == '__main__':
    main()
