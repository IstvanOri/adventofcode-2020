import unittest

from ac2020.days.Day2 import Day2


class Day2Test(unittest.TestCase):

    def test_empty_input(self):
        day = Day2()
        day._set_input('')
        self.assertEqual('No result', day.part1())
        self.assertEqual('No result', day.part2())

    def test_correct_input(self):
        day = Day2()
        day._set_input('1-3 a: abcde\n1-3 b: cdefg\n2-9 c: ccccccccc')
        self.assertEqual('2', day.part1())
        self.assertEqual('1', day.part2())

    def test_corrupted_input(self):
        day = Day2()
        day._set_input('1-3 a: abcde asd\n1-3\n2-9 c: ccccccccc')
        self.assertEqual('No result', day.part1())
        self.assertEqual('No result', day.part2())
