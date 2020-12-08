import unittest

from ac2020.days.Day6 import Day6


class Day6Test(unittest.TestCase):

    def test_empty_input(self):
        day = Day6()
        day._set_input('')
        self.assertEqual('0', day.part1())
        self.assertEqual('0', day.part2())

    def test_correct_input(self):
        day = Day6()
        day._set_input('abc\n\na\nb\nc\n\nab\nac\n\na\na\na\na\n\nb')
        self.assertEqual('11', day.part1())
        self.assertEqual('6', day.part2())
