from collections import defaultdict
from copy import deepcopy

from ac2020.days import AbstractDay
from ac2020.io import InputReader


def active_neighbors3(cubes, coord):
    count = 0
    for x in range(-1, 2):
        for y in range(-1, 2):
            for z in range(-1, 2):
                if x == 0 and y == 0 and z == 0:
                    continue
                c = (coord[0] + x, coord[1] + y, coord[2] + z)
                if c in cubes and cubes[c] == 1:
                    count += 1
    return count


def active_neighbors4(cubes, coord):
    count = 0
    for x in range(-1, 2):
        for y in range(-1, 2):
            for z in range(-1, 2):
                for w in range(-1, 2):
                    if x == 0 and y == 0 and z == 0 and w == 0:
                        continue
                    c = (coord[0] + x, coord[1] + y, coord[2] + z, coord[3] + w)
                    if c in cubes and cubes[c] == 1:
                        count += 1
    return count


def init_neighbors3(cubes, coord):
    for x in range(-1, 2):
        for y in range(-1, 2):
            for z in range(-1, 2):
                c = (coord[0] + x, coord[1] + y, coord[2] + z)
                if cubes[c] != 1:
                    cubes[c] = 0


def init_neighbors4(cubes, coord):
    for x in range(-1, 2):
        for y in range(-1, 2):
            for z in range(-1, 2):
                for w in range(-1, 2):
                    c = (coord[0] + x, coord[1] + y, coord[2] + z, coord[3] + w)
                    if cubes[c] != 1:
                        cubes[c] = 0


class Day17(AbstractDay.AbstractDay):
    """
    Advent of Code 2020 - Day 17
    ============================
    """

    def _set_input(self, input_: str):
        self.entries = InputReader.read_character_matrix(input_)

    def part1(self) -> str:
        cubes = defaultdict(int)
        for y in range(len(self.entries)):
            for x in range(len(self.entries[y])):
                if self.entries[y][x] == '#':
                    cubes[(x, y, 0)] = 1

        for i in range(6):
            work_with = deepcopy(cubes)
            for coord in work_with:
                init_neighbors3(cubes, coord)
            work_with = deepcopy(cubes)
            for coord in work_with:
                if work_with[coord] == 1:
                    if not (2 <= active_neighbors3(work_with, coord) <= 3):
                        cubes[coord] = 0
                else:
                    if active_neighbors3(work_with, coord) == 3:
                        cubes[coord] = 1
        return str(sum(cubes.values()))

    def part2(self) -> str:
        cubes = defaultdict(int)
        for y in range(len(self.entries)):
            for x in range(len(self.entries[y])):
                if self.entries[y][x] == '#':
                    cubes[(x, y, 0, 0)] = 1

        for i in range(6):
            work_with = deepcopy(cubes)
            for coord in work_with:
                init_neighbors4(cubes, coord)
            work_with = deepcopy(cubes)
            for coord in work_with:
                if work_with[coord] == 1:
                    if not (2 <= active_neighbors4(work_with, coord) <= 3):
                        cubes[coord] = 0
                else:
                    if active_neighbors4(work_with, coord) == 3:
                        cubes[coord] = 1
        return str(sum(cubes.values()))
