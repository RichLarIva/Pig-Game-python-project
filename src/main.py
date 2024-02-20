# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Lets play a game of "Pig (dice game)".

Will throw a singular dice between 1 and 6.

"""

import shell


def main():
    """Executes the main program."""
    print(__doc__)
    shell_instance = shell.Shell
    shell_instance.cmdloop()


if __name__ == "__main__":
    main()
