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

    histgram = histogram
    player_data = player
    ai = intelligence
    is_player_turn = True
    intro = "Welcome to the src. Type help or ? to list commands.\n"
    prompt = "(game) "
    current_score = 0

    def __init__(self, target_score=100):
        super().__init__()
        self.game = game.Game()
        self.dice = dice.Dice()
        self.histgram = histogram.Histogram()
        self.target_score = target_score
        player_name = input("Whats your name? ")
        self.player_data = player.Player(player_name)
        self.ai = intelligence.Intelligence()

    def do_start(self, _):
        """Start the game with the player throwing the dice."""
        message = "You will start throwing the dice.\nYou managed to roll {}"
        self.game.start()
        self.dice.throw()
        print(message.format(self.dice.current_number))
        self.histgram.record_roll(self.dice.current_number)
        if self.dice.current_number == 1:
            for roll in self.ai.play_turn(True):
                self.histgram.record_roll(roll)
        else:
            self.player_data.add_to_score(self.dice.current_number)


    def do_throw(self, arg):
        """Throw the dice."""
        self.dice.throw()
        print("You rolled:", self.dice.current_number)
        self.histgram.record_roll(self.dice.current_number)
        if self.dice.current_number == 1:
            for roll in self.ai.play_turn(True):
                self.histgram.record_roll(roll)
        else:
            self.player_data.add_to_score(self.dice.current_number)


    def do_switch_turn(self, _):
        """Switches turn."""
        for roll in self.ai.play_turn(True):
            self.histgram.record_roll(roll)

    def do_show_histogram(self, _):
        """Shows the histogram."""
        self.histgram.display()

    def do_score(self, _):
        print(f"Current scores:\n{self.player_data.name}\tAI\n{self.player_data.score}\t{self.ai.score}")

    def do_exit(self, arg):
        """Leave the game."""
        print("Hope you enjoyed the game.")
        return True

    def do_q(self, arg):
        """Leave the game."""
        return self.do_exit(arg)

    def do_EOF(self, arg):
        """Leave the game."""
        return self.do_exit(arg)


if __name__ == "__main__":
    print(__doc__)
    shell = Shell()
    shell.cmdloop()
