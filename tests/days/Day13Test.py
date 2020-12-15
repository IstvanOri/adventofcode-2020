import unittest

from ac2020.days.Day13 import Day13


class Day13Test(unittest.TestCase):

    def test_empty_input(self):
        day = Day13()
        day._set_input('')
        self.assertEqual('No result', day.part1())
        self.assertEqual('No result', day.part2())

    def test_correct_input(self):
        day = Day13()
        day._set_input('939\n7,13,x,x,59,x,31,19')
        self.assertEqual('295', day.part1())
        self.assertEqual('1068781', day.part2())

    def test_mor_complicated_input(self):
        day = Day13()
        day._set_input('939\n1789,37,47,1889')
        self.assertEqual('47', day.part1())
        self.assertEqual('1202161486', day.part2())
