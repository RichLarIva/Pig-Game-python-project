#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""

import unittest
from unittest import mock
from src import histogram


class TestHistogramClass(unittest.TestCase):
    """Test the class."""

    test_histogram = histogram.Histogram()

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        res = histogram.Histogram()
        self.assertIsInstance(res, histogram.Histogram)

    def test_record_roll(self):
        """Record multiple rolls and see if the histogram is correct."""
        test_histogram = histogram.Histogram()
        test_histogram.record_roll(1)
        test_histogram.record_roll(2)
        test_histogram.record_roll(3)
        test_histogram.record_roll(1)
        test_histogram.record_roll(2)

        expected_histogram = {1: 2, 2: 2, 3: 1}
        self.assertEqual(test_histogram.histogram, expected_histogram)

    def test_display(self):
        """Tests the display."""
        test_histogram = histogram.Histogram()
        test_histogram.record_roll(1)
        test_histogram.record_roll(2)
        test_histogram.record_roll(3)
        test_histogram.record_roll(1)
        test_histogram.record_roll(2)
        test_histogram.record_roll(3)

        expected_output = "Dice Roll Histogram:"
        with unittest.mock.patch("builtins.print") as mock_print:
            self.test_histogram.display()
            mock_print.assert_called_once_with(expected_output)


if __name__ == "__main__":
    unittest.main()
