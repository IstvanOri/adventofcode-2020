import unittest

from ac2020.days.Day22 import Day22


class Day22Test(unittest.TestCase):

    def test_empty_input(self):
        day = Day22()
        day._set_input('')
        self.assertEqual('0', day.part1())
        self.assertEqual('0', day.part2())

    def test_correct_input(self):
        day = Day22()
        day._set_input('Player 1:\n9\n2\n6\n3\n1\n\nPlayer 2:\n5\n8\n4\n7\n10')
        self.assertEqual('306', day.part1())
        self.assertEqual('291', day.part2())
