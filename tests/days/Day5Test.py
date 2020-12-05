import unittest

from ac2020.days.Day5 import Day5


class Day5Test(unittest.TestCase):

    def test_empty_input(self):
        day = Day5()
        day._set_input('')
        self.assertEqual('0', day.part1())
        self.assertEqual('No result', day.part2())

    def test_correct_input(self):
        day = Day5()
        day._set_input('FBFBBFFRLR\nFBFBBFFLRR')
        self.assertEqual('357', day.part1())
        self.assertEqual('356', day.part2())
