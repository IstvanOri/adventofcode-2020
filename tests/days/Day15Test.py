import unittest

from ac2020.days.Day15 import Day15


class Day15Test(unittest.TestCase):

    def test_empty_input(self):
        day = Day15()
        day._set_input('')
        self.assertEqual('No result', day.part1())
        self.assertEqual('No result', day.part2())

    def test_correct_input(self):
        day = Day15()
        day._set_input('0,3,6')
        self.assertEqual('436', day.part1())
        self.assertEqual('175594', day.part2())
