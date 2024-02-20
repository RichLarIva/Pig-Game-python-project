#!/usr/bin/env python3
# -*- coding: utf-16 -*-

"""Using the cmd module to create a shell for the main program.

You can read about the cmd module in the docs:
    cmd — support for line-oriented command interpreters
    https://docs.python.org/3/library/cmd.html
"""

import cmd
import game

class Shell(cmd.Cmd):
    """The shell for handling commands and such"""
    intro = "Welcome to the game. Type help or ? to list commands.\n"
    prompt = "(game) "

    def __init__(self):
        super().__init__()
        self.game = game.Game()

    def do_start(self, _):
        """Start the game with the player throwing the dice"""
        message = (
            "You will start throwing the dice"
            " you managed to roll {}"
        )
        self.game.start()
        self.dice.throw()
        print(message.format(self.dice.current_number))

    def do_throw(self, arg):
        self.dice.throw()
        print(self.dice.current_number)

    def do_exit(self, _):
        # pylint: disable=no-self-use
        """Leave the game."""
        print("Hope you enjoyed the game.")
        return True
    def do_q(self, arg):
        """Leave the game."""
        return self.do_exit(arg)

    def do_EOF(self, arg):
        #pylint: disable=invalid-name
        """Leave the game."""
        return self.do_exit(arg)