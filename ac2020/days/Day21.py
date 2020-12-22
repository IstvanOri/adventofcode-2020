from collections import defaultdict

from ac2020.days import AbstractDay
from ac2020.io import InputReader


class Day21(AbstractDay.AbstractDay):

    def _set_input(self, input_: str):
        self.entries = {}
        self.ingredients = []
        self.foods = []
        self.allergens = []
        self.part2_result = ''
        if len(input_) != 0:
            lines = InputReader.read_line_by_line(input_)
            for line in lines:
                split = line.split(' (')
                self.foods.append(split[0].split())
                for x in split[0].split():
                    self.ingredients.append(x)
                self.allergens.append(split[1].replace(')', '').replace('contains ', '').split(', '))

    def part1(self):
        possibilities = defaultdict(set)
        dangerous = {}
        allergen_foods = set()
        for i in range(len(self.foods)):
            for allergen in self.allergens[i]:
                if len(possibilities[allergen]) == 0:
                    possibilities[allergen] = set(self.foods[i])
                else:
                    possibilities[allergen] = possibilities[allergen].intersection(set(self.foods[i]))
        for allergen_food in allergen_foods:
            for possibility in possibilities:
                if allergen_food in possibilities[possibility]:
                    possibilities[possibility].remove(allergen_food)
        changed = True
        while changed:
            changed = False
            for possibility in possibilities:
                if len(possibilities[possibility]) == 1:
                    changed = True
                    allergen = possibilities[possibility].pop()
                    dangerous[possibility] = allergen
                    allergen_foods.add(allergen)
            for allergen_food in allergen_foods:
                for possibility in possibilities:
                    if allergen_food in possibilities[possibility]:
                        possibilities[possibility].remove(allergen_food)

        non_allergens = set(self.ingredients) - set(allergen_foods)
        i = 0
        for food in self.foods:
            i += len(set(food).intersection(non_allergens))
        for name in sorted(dangerous):
            if len(self.part2_result) != 0:
                self.part2_result += ','
            self.part2_result += dangerous[name]
        return str(i)

    def part2(self):
        return self.part2_result
