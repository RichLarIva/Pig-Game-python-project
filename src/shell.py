# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Using the cmd module to create a shell for the main program.

You can read about the cmd module in the docs:
    cmd - support for line-oriented command interpreters
    https://docs.python.org/3/library/cmd.html
"""

import cmd
import game
import dice


class Shell(cmd.Cmd):
    """The shell for handling commands and such"""

    intro = "Welcome to the src. Type help or ? to list commands.\n"
    prompt = "(game) "

    def __init__(self):
        super().__init__()
        self.game = game.Game()
        self.dice = dice.Dice()

    def do_start(self, arg):
        """Start the src with the player throwing the dice"""
        message = "You will start throwing the dice. You managed to roll {}"
        self.dice.throw()
        print(message.format(self.dice.current_number))

    def do_throw(self, arg):
        """Throw the dice"""
        self.dice.throw()
        print("You rolled:", self.dice.current_number)

    def do_exit(self, arg):
        """Leave the src."""
        print("Hope you enjoyed the src.")
        return True

    def do_q(self, arg):
        """Leave the src."""
        return self.do_exit(arg)

    def do_EOF(self, arg):
        """Leave the src."""
        return self.do_exit(arg)
