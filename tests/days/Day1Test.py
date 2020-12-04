import unittest

from ac2020.days.Day1 import Day1


class Day1Test(unittest.TestCase):

    def test_empty_input(self):
        day = Day1()
        day._set_input("")
        self.assertEqual("No result", day.part1())
        self.assertEqual("No result", day.part2())

    def test_correct_input(self):
        day = Day1()
        day._set_input("1721 979 366 299 675 1456")
        self.assertEqual("514579", day.part1())
        self.assertEqual("241861950", day.part2())

    def test_tricky_input(self):
        """
        1010 + 1010 could result in 2020, but an entry only can be used once.

        Same for 1010 + 505 + 505.
        """
        day = Day1()
        day._set_input("1010 505")
        self.assertEqual("No result", day.part1())
        self.assertEqual("No result", day.part2())

    def test_non_numeric_input(self):
        day = Day1()
        day._set_input("1 15 30 40 2019 asd 1975")
        self.assertEqual("No result", day.part1())
        self.assertEqual("No result", day.part2())
