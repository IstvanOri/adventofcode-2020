import unittest

from ac2020.days.Day19 import Day19


class Day19Test(unittest.TestCase):

    def test_empty_input(self):
        day = Day19()
        day._set_input('')
        self.assertEqual('0', day.part1())
        self.assertEqual('0', day.part2())

    def test_correct_input(self):
        day = Day19()
        day._set_input('abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa\nbbabbbbaabaabba\nbabbbbaabbbbbabbbbbbaabaaabaaa\naaabbbbbbaaaabaababaabababbabaaabbababababaaa\nbbbbbbbaaaabbbbaaabbabaaa\nbbbababbbbaaaaaaaabbababaaababaabab\nababaaaaaabaaab\nababaaaaabbbaba\nbaabbaaaabbaaaababbaababb\nabbbbabbbbaaaababbbbbbaaaababb\naaaaabbaabaaaaababaa\naaaabbaaaabbaaa\naaaabbaabbaaaaaaabbbabbbaaabbaabaaa\nbabaaabbbaaabaababbaabababaaab\naabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba')
        self.assertEqual('3', day.part1())
        self.assertEqual('12', day.part2())
