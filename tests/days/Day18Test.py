import unittest

from ac2020.days.Day18 import Day18


class Day18Test(unittest.TestCase):

    def test_empty_input(self):
        day = Day18()
        day._set_input('')
        self.assertEqual('0', day.part1())
        self.assertEqual('0', day.part2())

    def test_correct_input_51(self):
        day = Day18()
        day._set_input('1 + (2 * 3) + (4 * (5 + 6))')
        self.assertEqual('51', day.part1())
        self.assertEqual('51', day.part2())
