import unittest

from algo import staircases


class StaircaseTest(unittest.TestCase):
    def test_given_3_should_print_h_3_lines(self):
        n = 3
        printed_sym = "#"
        expected_result = "  #\n" + " ##\n" + "###"

        result = staircases.staircase(n)

        self.assertEqual(len(expected_result.split("\n")), n)
        self.assertIn(printed_sym, expected_result)
        self.assertEqual(result, expected_result)