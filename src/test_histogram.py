#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""

import unittest
import histogram


class TestHistogramClass(unittest.TestCase):
    """Test the class."""

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        res = histogram.Histogram()
        exp = histogram.Histogram()
        self.assertIsInstance(res, exp)

    def test_record_roll(self):
        """Record multiple rolls and see if the histogram is correct."""
        test_histogram = Histogram()
        test_histogram.record_roll(1)
        test_histogram.record_roll(2)
        test_histogram.record_roll(3)
        test_histogram.record_roll(1)
        test_histogram.record_roll(2)
        test_histogram.record_roll(3)
        test_histogram.record_roll(1)
        test_histogram.record_roll(2)
        test_histogram.record_roll(3)

        expected_histogram = {1: 3, 2: 3, 3: 3}
        self.assertEqual(test_histogram.Histogram(), expected_histogram)

    def test_display(self):
        """Tests the display."""
        test_histogram = Histogram()
        histogram.record_roll(1)
        histogram.record_roll(2)
        histogram.record_roll(3)
        histogram.record_roll(1)
        histogram.record_roll(2)
        histogram.record_roll(3)

        expected_output = "Dice Roll Histogram:\n1: ***\n2: ***\n3: ***\n"
        with unittest.mock.patch("builtins.print") as mock_print:
            histogram.display()
            mock_print.assert_called_once_with(expected_output)


if __name__ == "__main__":
    unittest.main()
