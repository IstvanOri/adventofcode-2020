import unittest

from ac2020.days.Day11 import Day11


class Day11Test(unittest.TestCase):

    def test_empty_input(self):
        day = Day11()
        day._set_input('')
        self.assertEqual('0', day.part1())
        self.assertEqual('0', day.part2())

    def test_correct_input(self):
        day = Day11()
        day._set_input('L.LL.LL.LL\nLLLLLLL.LL\nL.L.L..L..\nLLLL.LL.LL\nL.LL.LL.LL\nL.LLLLL.LL\n..L.L.....\nLLLLLLLLLL\nL.LLLLLL.L\nL.LLLLL.LL')
        self.assertEqual('37', day.part1())
        self.assertEqual('26', day.part2())