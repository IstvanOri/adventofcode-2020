import unittest

from ac2020.days.Day10 import Day10


class Day10Test(unittest.TestCase):

    def test_empty_input(self):
        day = Day10()
        day._set_input('')
        self.assertEqual('No result', day.part1())
        self.assertEqual('No result', day.part2())

    def test_correct_input(self):
        day = Day10()
        day._set_input('16\n10\n15\n5\n1\n11\n7\n19\n6\n12\n4')
        self.assertEqual('35', day.part1())
        self.assertEqual('8', day.part2())

    def test_more_complex_correct_input(self):
        day = Day10()
        day._set_input('28\n33\n18\n42\n31\n14\n46\n20\n48\n47\n24\n23\n49\n45\n19\n38\n39\n11\n1\n32\n25\n35\n8\n17\n7\n9\n4\n2\n34\n10\n3')
        self.assertEqual('220', day.part1())
        self.assertEqual('19208', day.part2())