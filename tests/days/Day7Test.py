import unittest

from ac2020.days.Day7 import Day7


class Day7Test(unittest.TestCase):

    def test_empty_input(self):
        day = Day7()
        day._set_input('')
        self.assertEqual('0', day.part1())
        self.assertEqual('No result', day.part2())

    def test_correct_input(self):
        day = Day7()
        day._set_input('light red bags contain 1 bright white bag, 2 muted yellow bags.\ndark orange bags contain 3 bright white bags, 4 muted yellow bags.\nbright white bags contain 1 shiny gold bag.\nmuted yellow bags contain 2 shiny gold bags, 9 faded blue bags.\nshiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.\ndark olive bags contain 3 faded blue bags, 4 dotted black bags.\nvibrant plum bags contain 5 faded blue bags, 6 dotted black bags.\nfaded blue bags contain no other bags.\ndotted black bags contain no other bags.')
        self.assertEqual('4', day.part1())
        self.assertEqual('32', day.part2())

    def test_correct_input2(self):
        day = Day7()
        day._set_input('shiny gold bags contain 2 dark red bags.\ndark red bags contain 2 dark orange bags.\ndark orange bags contain 2 dark yellow bags.\ndark yellow bags contain 2 dark green bags.\ndark green bags contain 2 dark blue bags.\ndark blue bags contain 2 dark violet bags.\ndark violet bags contain no other bags.')
        self.assertEqual('0', day.part1())
        self.assertEqual('126', day.part2())
