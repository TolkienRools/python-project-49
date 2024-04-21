#!/usr/bin/env python3
from brain_games import tools


def main():
    name = tools.greeting()
    tools.even_quiz(name)


if __name__ == '__main__':
    main()
