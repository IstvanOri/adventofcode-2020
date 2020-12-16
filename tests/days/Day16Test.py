import unittest

from ac2020.days.Day16 import Day16


class Day16Test(unittest.TestCase):

    def test_empty_input(self):
        day = Day16()
        day._set_input('')
        self.assertEqual('No result', day.part1())
        self.assertEqual('No result', day.part2())

    def test_correct_input_for_part1(self):
        day = Day16()
        day._set_input('class: 1-3 or 5-7\nrow: 6-11 or 33-44\nseat: 13-40 or 45-50\n\nyour ticket:\n7,1,14\n\nnearby tickets:\n7,3,47\n40,4,50\n55,2,20\n38,6,12')
        self.assertEqual('71', day.part1())

    def test_correct_input_for_part2_without_interesting_fields(self):
        day = Day16()
        day._set_input('class: 0-1 or 4-19\nrow: 0-5 or 8-19\nseat: 0-13 or 16-19\n\nyour ticket:\n11,12,13\n\nnearby tickets:\n3,9,18\n15,1,5\n5,14,9')
        self.assertEqual('No result', day.part2())

    def test_correct_input_for_part2_with_interesting_fields(self):
        day = Day16()
        day._set_input('departure location: 0-1 or 4-19\nrow: 0-5 or 8-19\ndeparture track: 0-13 or 16-19\n\nyour ticket:\n11,12,13\n\nnearby tickets:\n3,9,18\n15,1,5\n5,14,9')
        self.assertEqual('156', day.part2())
