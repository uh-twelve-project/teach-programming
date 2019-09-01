#!/usr/bin/env python3

from turtle import *
from cmd import Cmd

from config import *


t = Turtle()


class cmd(Cmd):
    intro = 'Welcome to the turtle shell.   Type help or ? to list commands.\n'
    prompt = '(turtle) '

    def do_help(self, line):
        print('hello')

    def do_EOF(self, line):
        print('^D')
        return True


def main():
    cmd().cmdloop()


if __name__ == "__main__":
    main()
