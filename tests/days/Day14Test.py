import unittest

from ac2020.days.Day14 import Day14


class Day14Test(unittest.TestCase):

    def test_empty_input(self):
        day = Day14()
        day._set_input('')
        self.assertEqual('0', day.part1())
        self.assertEqual('0', day.part2())

    def test_correct_input_for_part1(self):
        day = Day14()
        day._set_input('mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X\nmem[8] = 11\nmem[7] = 101\nmem[8] = 0')
        self.assertEqual('165', day.part1())

    def test_correct_input_for_part2(self):
        day = Day14()
        day._set_input('mask = 000000000000000000000000000000X1001X\nmem[42] = 100\nmask = 00000000000000000000000000000000X0XX\nmem[26] = 1')
        self.assertEqual('208', day.part2())
