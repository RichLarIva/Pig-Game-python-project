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
import player
import intelligence

class Shell(cmd.Cmd):
    """The shell for handling commands and such"""
    player_data = player
    ai = intelligence
    is_player_turn = True
    intro = "Welcome to the src. Type help or ? to list commands.\n"
    prompt = "(game) "

    def __init__(self, target_score=100):
        super().__init__()
        self.game = game.Game()
        self.dice = dice.Dice()
        self.target_score = target_score


    def do_start(self, _):
        """Start the game with the player throwing the dice"""
        player_name = input("Whats your name? ")
        self.player_data = player.Player(player_name)
        self.ai = intelligence.Intelligence()
        message = "You will start throwing the dice.\nYou managed to roll {}"
        self.game.start()
        self.dice.throw()
        print(message.format(self.dice.current_number))

    def do_throw(self, arg):
        """Throw the dice"""
        self.dice.throw()
        print("You rolled:", self.dice.current_number)
        histogram.Histogram.record_roll(self.dice.current_number)

    def do_switch_turn(self, _):
        """Switches turn"""
        self.ai.play_turn()

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
    print(__doc__)
    shell = Shell()
    shell.cmdloop()