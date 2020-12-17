import unittest

from ac2020.days.Day17 import Day17


class Day17Test(unittest.TestCase):

    def test_empty_input(self):
        day = Day17()
        day._set_input('')
        self.assertEqual('0', day.part1())
        self.assertEqual('0', day.part2())

    def test_correct_input(self):
        day = Day17()
        day._set_input('.#.\n..#\n###')
        self.assertEqual('112', day.part1())
        self.assertEqual('848', day.part2())
