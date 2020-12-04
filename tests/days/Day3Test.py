import unittest

from ac2020.days.Day3 import Day3


class Day3Test(unittest.TestCase):

    def test_empty_input(self):
        day = Day3()
        day._set_input('')
        self.assertEqual('0', day.part1())
        self.assertEqual('0', day.part2())

    def test_correct_input(self):
        day = Day3()
        day._set_input('..##.......\n#...#...#..\n.#....#..#.\n..#.#...#.#\n.#...##..#.\n..#.##.....\n.#.#.#....#\n.#........#\n#.##...#...\n#...##....#\n.#..#...#.#')
        self.assertEqual('7', day.part1())
        self.assertEqual('336', day.part2())