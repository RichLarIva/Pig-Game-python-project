# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Lets play a game of "Pig (dice game)".

Will throw a singular dice between 1 and 6.

"""

import cmd
import game
import dice
import histogram

class Shell(cmd.Cmd):
    """The shell for handling commands and such"""

    intro = "Welcome to the src. Type help or ? to list commands.\n"
    prompt = "(game) "

    def __init__(self):
        super().__init__()
        self.game = game.Game()
        self.dice = dice.Dice()

    def do_start(self, _):
        """Start the src with the player throwing the dice"""
        message = "You will start throwing the dice.\nYou managed to roll {}"
        self.game.start()
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

if __name__ == "__main__":
    shell = Shell()
    shell.cmdloop()