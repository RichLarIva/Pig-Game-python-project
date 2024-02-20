# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Lets play a src of "Pig (dice src)".

Will throw a singular dice between 1 and 6.

"""

import shell
import histogram


def main():
    """Executes the main program."""
    print(__doc__)
    shell_instance = shell.Shell
    shell_instance.cmdloop()
    test_histogram = histogram.Histogram()

    # record some dice rolls
    rolls = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3]
    for roll in rolls:
        test_histogram.record_roll(roll)

    test_histogram.display()


if __name__ == "__main__":
    main()
