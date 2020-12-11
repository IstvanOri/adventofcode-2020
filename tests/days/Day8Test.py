import unittest

from ac2020.days.Day8 import Day8


class Day8Test(unittest.TestCase):

    def test_empty_input(self):
        day = Day8()
        day._set_input('')
        self.assertEqual('No result', day.part1())
        self.assertEqual('No result', day.part2())

    def test_empty_input(self):
        day = Day8()
        day._set_input('nop +0\nacc +1\njmp +4\nacc +3\njmp -3\nacc -99\nacc +1\njmp -4\nacc +6')
        self.assertEqual('Infinite: 5', day.part1())
        self.assertEqual('Terminated: 8', day.part2())
