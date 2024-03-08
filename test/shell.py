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
    """The shell for handling commands and such, also is the main class."""

    histgram = histogram
    player_data = player
    ai = intelligence
    is_player_turn = True
    intro = "Welcome to the src. Type help or ? to list commands.\n"
    prompt = "(game) "
    current_score = 0
    has_started = False

    def __init__(self, target_score=100):
        super().__init__()
        self.game = game.Game()
        self.dice = dice.Dice()
        self.histgram = histogram.Histogram()
        self.target_score = target_score
        player_name = input("Whats your name? ")
        self.player_data = player.Player(player_name)
        self.ai = intelligence.Intelligence()
        self.has_started = False

    def do_start(self, _):
        """Start the game with the player throwing the dice."""
        if self.has_started is False:
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

            self.has_started = True
        else:
            print("You have already started the game.")

    def do_throw(self, arg):
        """Throw the dice."""
        if self.has_started is False:
            print("You have to start the game.")

        elif self.has_started is True:
            self.dice.throw()
            print("You rolled:", self.dice.current_number)
            self.histgram.record_roll(self.dice.current_number)
            if self.dice.current_number == 1:
                for roll in self.ai.play_turn(True):
                    self.histgram.record_roll(roll)
            else:
                self.player_data.add_to_score(self.dice.current_number)
            if self.player_data.score >= self.target_score:
                print(f"{self.player_data.name} won with {self.player_data.score}!")
                self.histgram.display()
                self.has_started = False
            if self.ai.score >= self.target_score:
                print(f"The AI won with {self.ai.score}!")
                self.do_score()
                self.histgram.display()
                self.has_started = False

    def do_switch_turn(self, _):
        """Switches turn."""
        if self.has_started is True:
            for roll in self.ai.play_turn(True):
                self.histgram.record_roll(roll)
        else:
            print("You have to start the game.")
        if self.ai.score >= self.target_score:
            print(f"The AI won with {self.ai.score}!")
            self.do_score()
            self.histgram.display()
            self.has_started = False
        if self.player_data.score >= self.target_score:
            print(f"{self.player_data.name} won with {self.player_data.score}!")
            self.histgram.display()
            self.has_started = False

    def do_show_histogram(self, _):
        """Shows the histogram."""
        self.histgram.display()

    def do_score(self, _):
        """Shows the current scores"""
        print(
            f"Current scores:\n{self.player_data.name}\tAI\n{self.player_data.score}\t{self.ai.score}"
        )

    def do_cheat(self, _):
        """Lets the player cheat."""
        print("So you want to cheat?\n Alright I will let you gain some extra score and lower the score to 50.")
        self.target_score = 50
        self.player_data.score += 10

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

    def do_rules(self, _):
        """Shows the rules to the player."""
        print("The rules for this game are simple:\n You can throw a dice until it reaches one where it it switches over to the AI's turn to play\n or you can before reaching a one switch turn\nFirst one to reach 100 wins.")

if __name__ == "__main__":
    print(__doc__)
    shell = Shell()
    shell.cmdloop()
