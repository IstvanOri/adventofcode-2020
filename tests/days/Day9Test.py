import unittest

from ac2020.days.Day9 import Day9


class Day9Test(unittest.TestCase):

    def test_empty_input(self):
        day = Day9()
        day._set_input('')
        self.assertEqual('No result', day.part1())
        self.assertEqual('No result', day.part2())

    def test_correct_input(self):
        day = Day9()
        day._PREAMBLE_ = 5
        day._set_input('35\n20\n15\n25\n47\n40\n62\n55\n65\n95\n102\n117\n150\n182\n127\n219\n299\n277\n309\n576')
        self.assertEqual('127', day.part1())
        self.assertEqual('62', day.part2())
