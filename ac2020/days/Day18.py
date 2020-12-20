import re
from collections import deque

from ac2020.days import AbstractDay


def translate_to_polish(s):
    """
    Transforms a mathematical expression (containing natural numbers, +, *, and parenthesis) to Polish Notation.
    https://en.wikipedia.org/wiki/Polish_notation

    The exact implementation of the abstract program from Algorithms and Data Structures course (ELTE).
    Sorry, hungarian only: https://people.inf.elte.hu/veanna/alg1/segedanyagok/LengyelForma/index.htm

    :return: The Polish Notation of a plain mathematical expression
    """
    result = []
    stack = deque()
    for c in s.replace('(', '( ').replace(')', ' )').split(' '):
        if c == '(':
            stack.append(c)
        elif c == ')':
            if len(stack) > 0:
                top = stack.pop()
                while top != '(' and len(stack) != 0:
                    result.append(top)
                    top = stack.pop()
        elif c == '+':
            if len(stack) > 0:
                top = stack.pop()
                stack.append(top)
                while len(stack) > 0 and top != '(' and top != '*':
                    result.append(stack.pop())
                    if len(stack) > 0:
                        top = stack.pop()
                        stack.append(top)
            stack.append('+')
        elif c == '*':
            if len(stack) > 0:
                top = stack.pop()
                stack.append(top)
                while len(stack) > 0 and top != '(':
                    result.append(stack.pop())
                    if len(stack) > 0:
                        top = stack.pop()
                        stack.append(top)
            stack.append(c)
        else:
            stack.append(c)
    while len(stack) != 0:
        result.append(stack.pop())
    return result


def evaluate_polish(pol):
    """
    Evaluates an arithmetical expression written in Polish Notation.

    :result: The result of an expression written in Polish Notation.
    """
    tokens = list(pol)
    stack = []

    for token in tokens:
        if token == '+':
            arg2 = int(stack.pop())
            arg1 = int(stack.pop())
            stack.append(arg1 + arg2)
        elif token == '*':
            arg2 = int(stack.pop())
            arg1 = int(stack.pop())
            stack.append(arg1 * arg2)
        else:
            stack.append(int(token))
    return stack.pop()


class Day18(AbstractDay.AbstractDay):
    """
    Advent of Code 2020 - Day 18
    ============================

    As you look out the window and notice a heavily-forested continent slowly appear over the horizon,
    you are interrupted by the child sitting next to you. They're curious if you could help them with their
    math homework.

    Unfortunately, it seems like this "math" follows different rules than you remember.

    The homework (your puzzle input) consists of a series of expressions that consist of addition (+),
    multiplication (*), and parentheses ((...)). Just like normal math, parentheses indicate that the
    expression inside must be evaluated before it can be used by the surrounding expression. Addition
    still finds the sum of the numbers on both sides of the operator, and multiplication still finds the product.

    However, the rules of operator precedence have changed. Rather than evaluating multiplication
    before addition, the operators have the same precedence, and are evaluated left-to-right regardless
    of the order in which they appear.

    For example, the steps to evaluate the expression 1 + 2 * 3 + 4 * 5 + 6 are as follows::

    1 + 2 * 3 + 4 * 5 + 6
      3   * 3 + 4 * 5 + 6
          9   + 4 * 5 + 6
             13   * 5 + 6
                 65   + 6
                     71

    Parentheses can override this order; for example, here is what happens
    if parentheses are added to form 1 + (2 * 3) + (4 * (5 + 6))::

    1 + (2 * 3) + (4 * (5 + 6))
    1 +    6    + (4 * (5 + 6))
         7      + (4 * (5 + 6))
         7      + (4 *   11   )
         7      +     44
                51

    Here are a few more examples::

    2 * 3 + (4 * 5) becomes 26.
    5 + (8 * 3 + 9 + 3 * 4 * 3) becomes 437.
    5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) becomes 12240.
    ((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 becomes 13632.

    Before you can help with the homework, you need to understand it yourself.
    Evaluate the expression on each line of the homework; what is the sum of the resulting values?

    --- Part Two ---
    ----------------

    You manage to answer the child's questions and they finish part 1 of their homework, but get
    stuck when they reach the next section: advanced math.

    Now, addition and multiplication have different precedence levels, but they're not the ones you're
    familiar with. Instead, addition is evaluated before multiplication.

    For example, the steps to evaluate the expression 1 + 2 * 3 + 4 * 5 + 6 are now as follows::

    1 + 2 * 3 + 4 * 5 + 6
      3   * 3 + 4 * 5 + 6
      3   *   7   * 5 + 6
      3   *   7   *  11
         21       *  11
             231

    Here are the other examples from above::

    1 + (2 * 3) + (4 * (5 + 6)) still becomes 51.
    2 * 3 + (4 * 5) becomes 46.
    5 + (8 * 3 + 9 + 3 * 4 * 3) becomes 1445.
    5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) becomes 669060.
    ((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 becomes 23340.

    What do you get if you add up the results of evaluating the homework problems using these new rules?
    """

    def _set_input(self, input_: str):
        self.entries = input_.split('\n')

    def part1(self) -> str:
        """
        Solving part one without using my brain. Handling the input character by character, the operands are
        read in a buffer digit by digit, and after an operand is fully read, the current part of the expression
        is evaluated. When a parenthesis is encountered, a new state is opened, the whole subexpression is
        evaluated and handled as a single operand.

        Yeah, I had this "genius" gut feeling sounding like this: "Polish Notation would be an overkill."

        :return: the sum of the results of each expression
        """
        sum_of_all = 0
        for entry in self.entries:
            characters = list(entry.replace(' ', ''))
            buffer = ''
            last_operator = ['+']
            result = [0]
            for i, c in enumerate(characters):
                if c == '+' or c == '*':
                    result[-1] = eval(str(result[-1]) + last_operator[-1] + buffer)
                    last_operator[-1] = c
                    buffer = ''
                elif c == '(':
                    result.append(0)
                    last_operator.append('+')
                elif c == ')':
                    result[-1] = eval(str(result[-1]) + last_operator[-1] + buffer)
                    last_operator.pop()
                    result[-2] = eval(str(result[-2]) + last_operator[-1] + str(result[-1]))
                    last_operator[-1] = ''
                    result.pop()
                    buffer = ''
                else:
                    buffer += c
                    if i == len(characters) - 1:
                        if last_operator[-1] == '+':
                            result[-1] += int(buffer)
                        if last_operator[-1] == '*':
                            result[-1] *= int(buffer)
            sum_of_all += result[0]
        return str(sum_of_all)

    def part2(self) -> str:
        """
        This time I've used my brain a bit. Just a bit, I've spent a lot more amount of time to bend my
        first solution to cover this part than I'm proud of. After that I"ve chosen the right path. Polish
        Notation rulz! I should've started with this.
        """
        sum_of_all = 0
        for entry in self.entries:
            if len(entry) == 0:
                continue
            polish = translate_to_polish(entry)
            evaluated = evaluate_polish(polish)
            sum_of_all += evaluated
        return str(sum_of_all)
