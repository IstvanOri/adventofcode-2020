import unittest

from ac2020.days.Day12 import Day12


class Day12Test(unittest.TestCase):

    def test_empty_input(self):
        day = Day12()
        day._set_input('')
        self.assertEqual('0', day.part1())
        self.assertEqual('0', day.part2())

    def test_correct_input(self):
        day = Day12()
        day._set_input('F10\nN3\nF7\nR90\nF11')
        self.assertEqual('25', day.part1())
        self.assertEqual('286', day.part2())
