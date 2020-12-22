import unittest

from ac2020.days.Day21 import Day21


class Day21Test(unittest.TestCase):

    def test_empty_input(self):
        day = Day21()
        day._set_input('')
        self.assertEqual('0', day.part1())
        self.assertEqual('', day.part2())

    def test_correct_input(self):
        day = Day21()
        day._set_input('mxmxvkd kfcds sqjhc nhms (contains dairy, fish)\ntrh fvjkl sbzzf mxmxvkd (contains dairy)\nsqjhc fvjkl (contains soy)\nsqjhc mxmxvkd sbzzf (contains fish)')
        self.assertEqual('5', day.part1())
        self.assertEqual('mxmxvkd,sqjhc,fvjkl', day.part2())
