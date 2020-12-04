from abc import ABC
from sys import stdin


class AbstractDay(ABC):
    """
    Abstract class for Days, each day should extend this class.

    Always override these functions:
     - _set_input
     - part1
     - part2
    """

    def read_input(self):
        print('Provide input (Ctrl+D to terminate): ')
        self._set_input(stdin.read())

    def _set_input(self, input_: str):
        """
        Sets the input for the instance. Sanitation can be performed here.

        :param input_: the raw input
        """
        pass

    def part1(self) -> str:
        """
        Generates the solution for the first part.
        """
        pass

    def part2(self) -> str:
        """
        Generates the solution for the second part.
        """
        pass
