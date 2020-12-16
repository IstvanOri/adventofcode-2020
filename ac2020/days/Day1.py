from itertools import combinations
from math import prod

from ac2020.days import AbstractDay
from ac2020.io import InputReader


class Day1(AbstractDay.AbstractDay):
    """
        Advent of Code 2020 - Day 1
        ===========================

        Before you leave, the Elves in accounting just need you to fix your **expense report** (your puzzle input);
        apparently, something isn't quite adding up.
        Specifically, they need you to **find the two entries that sum to 2020** and then multiply those two numbers
        together. For example, suppose your expense report contained the following::

            1721
            979
            366
            299
            675
            1456

        In this list, the two entries that sum to `2020` are `1721` and `299`.
        Multiplying them together produces `1721 * 299 = 514579`, so the correct answer is `514579`.

        --- Part Two ---
        ----------------

        The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left
        over from a past vacation. They offer you a second one if you can find three numbers in your expense report that
        meet the same criteria.

        Using the above example again, the three entries that sum to `2020` are `979`, `366`, and `675`. Multiplying
        them together produces the answer, `241861950`.

        In your expense report, **what is the product of the three entries that sum to `2020`**?
    """

    def _set_input(self, input_: str):
        """
        Setting up the input while converting the values to int.

        :param input_: the raw input.
        """
        self.entries = []
        try:
            self.entries = InputReader.read(input_, int)
        except ValueError:
            print('Every entry in the input has to be a number. No results for you!')


    def part1(self) -> str:
        """
        Solution for Day 1, part 1

        Getting every combination of three elements from the list of entries,
        checking the combinations for `(x + y = 2020)`, first passing combination provides the result.

        :return:
            x * y were x + y = 2020
        """
        return self.__find_result(2)

    def part2(self) -> str:
        """
        Solution for Day 1, part 2

        Getting every combination of three elements from the list of entries,
        checking the combinations for `(x + y + z = 2020)`, first passing combination provides the result.

        :return:
            x * y * z were x + y + z = 2020
        """
        return self.__find_result(3)

    def __find_result(self, combination: int) -> str:
        for i in combinations(self.entries, combination):
            if sum(i) == 2020:
                return str(prod(i))
        return 'No result'
