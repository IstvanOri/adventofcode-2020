import copy

from ac2020.days import AbstractDay


class Day11(AbstractDay.AbstractDay):
    """
    Advent of Code 2020 - Day 11
    ============================

    Your plane lands with plenty of time to spare. The final leg of your journey is a ferry that goes directly to
    the tropical island where you can finally start your vacation. As you reach the waiting area to board the ferry,
    you realize you're so early, nobody else has even arrived yet!

    By modeling the process people use to choose (or abandon) their seat in the waiting area, you're pretty sure
    you can predict the best place to sit. You make a quick map of the seat layout (your puzzle input).

    The seat layout fits neatly on a grid. Each position is either floor (.), an empty seat (L), or an
    occupied seat (#). For example, the initial seat layout might look like this::

    L.LL.LL.LL
    LLLLLLL.LL
    L.L.L..L..
    LLLL.LL.LL
    L.LL.LL.LL
    L.LLLLL.LL
    ..L.L.....
    LLLLLLLLLL
    L.LLLLLL.L
    L.LLLLL.LL

    Now, you just need to model the people who will be arriving shortly. Fortunately, people are entirely
    predictable and always follow a simple set of rules. All decisions are based on the number of occupied
    seats adjacent to a given seat (one of the eight positions immediately up, down, left, right, or diagonal
    from the seat). The following rules are applied to every seat simultaneously:

    If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
    If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
    Otherwise, the seat's state does not change.
    Floor (.) never changes; seats don't move, and nobody sits on the floor.

    After one round of these rules, every seat in the example layout becomes occupied::

    #.##.##.##
    #######.##
    #.#.#..#..
    ####.##.##
    #.##.##.##
    #.#####.##
    ..#.#.....
    ##########
    #.######.#
    #.#####.##

    After a second round, the seats with four or more occupied adjacent seats become empty again::

    #.LL.L#.##
    #LLLLLL.L#
    L.L.L..L..
    #LLL.LL.L#
    #.LL.LL.LL
    #.LLLL#.##
    ..L.L.....
    #LLLLLLLL#
    #.LLLLLL.L
    #.#LLLL.##

    This process continues for three more rounds::

    #.##.L#.##
    #L###LL.L#
    L.#.#..#..
    #L##.##.L#
    #.##.LL.LL
    #.###L#.##
    ..#.#.....
    #L######L#
    #.LL###L.L
    #.#L###.##
    #.#L.L#.##
    #LLL#LL.L#
    L.L.L..#..
    #LLL.##.L#
    #.LL.LL.LL
    #.LL#L#.##
    ..L.L.....
    #L#LLLL#L#
    #.LLLLLL.L
    #.#L#L#.##
    #.#L.L#.##
    #LLL#LL.L#
    L.#.L..#..
    #L##.##.L#
    #.#L.LL.LL
    #.#L#L#.##
    ..L.L.....
    #L#L##L#L#
    #.LLLLLL.L
    #.#L#L#.##

    At this point, something interesting happens: the chaos stabilizes and further applications of these rules cause
    no seats to change state! Once people stop moving around, you count 37 occupied seats.

    Simulate your seating area by applying the seating rules repeatedly until no seats change state. How many seats
    end up occupied?

    --- Part Two ---
    ----------------

    As soon as people start to arrive, you realize your mistake. People don't just care about adjacent seats - they
    care about the first seat they can see in each of those eight directions!

    Now, instead of considering just the eight immediately adjacent seats, consider the first seat in each of those
    eight directions. For example, the empty seat below would see eight occupied seats:

    .......#.
    ...#.....
    .#.......
    .........
    ..#L....#
    ....#....
    .........
    #........
    ...#.....

    The leftmost empty seat below would only see one empty seat, but cannot see any of the occupied ones::

    .............
    .L.L.#.#.#.#.
    .............

    The empty seat below would see no occupied seats::

    .##.##.
    #.#.#.#
    ##...##
    ...L...
    ##...##
    #.#.#.#
    .##.##.

    Also, people seem to be more tolerant than you expected: it now takes five or more visible occupied seats
    for an occupied seat to become empty (rather than four or more from the previous rules). The other rules
    still apply: empty seats that see no occupied seats become occupied, seats matching no rule don't
    change, and floor never changes.

    Given the same starting layout as above, these new rules cause the seating area to shift around as follows::

    L.LL.LL.LL
    LLLLLLL.LL
    L.L.L..L..
    LLLL.LL.LL
    L.LL.LL.LL
    L.LLLLL.LL
    ..L.L.....
    LLLLLLLLLL
    L.LLLLLL.L
    L.LLLLL.LL

    #.##.##.##
    #######.##
    #.#.#..#..
    ####.##.##
    #.##.##.##
    #.#####.##
    ..#.#.....
    ##########
    #.######.#
    #.#####.##

    #.LL.LL.L#
    #LLLLLL.LL
    L.L.L..L..
    LLLL.LL.LL
    L.LL.LL.LL
    L.LLLLL.LL
    ..L.L.....
    LLLLLLLLL#
    #.LLLLLL.L
    #.LLLLL.L#

    #.L#.##.L#
    #L#####.LL
    L.#.#..#..
    ##L#.##.##
    #.##.#L.##
    #.#####.#L
    ..#.#.....
    LLL####LL#
    #.L#####.L
    #.L####.L#

    #.L#.L#.L#
    #LLLLLL.LL
    L.L.L..#..
    ##LL.LL.L#
    L.LL.LL.L#
    #.LLLLL.LL
    ..L.L.....
    LLLLLLLLL#
    #.LLLLL#.L
    #.L#LL#.L#

    #.L#.L#.L#
    #LLLLLL.LL
    L.L.L..#..
    ##L#.#L.L#
    L.L#.#L.L#
    #.L####.LL
    ..#.#.....
    LLL###LLL#
    #.LLLLL#.L
    #.L#LL#.L#

    #.L#.L#.L#
    #LLLLLL.LL
    L.L.L..#..
    ##L#.#L.L#
    L.L#.LL.L#
    #.LLLL#.LL
    ..#.L.....
    LLL###LLL#
    #.LLLLL#.L
    #.L#LL#.L#

    Again, at this point, people stop shifting around and the seating area reaches equilibrium. Once this occurs,
    you count 26 occupied seats.

    Given the new visibility method and the rule change for occupied seats becoming empty, once equilibrium is
    reached, how many seats end up occupied?
    """

    def _set_input(self, input_: str):
        """
        Splitting the input by rows, and each row (strings) are converted to list, so the result is a list of list,
        where each 'cell' in the matrix is the state of a single seat.
        """
        self.entries = []
        if len(input_) != 0:
            self.entries = list(list(row) for row in input_.split('\n'))

    def part1(self) -> str:
        changed = True
        result = copy.deepcopy(self.entries)
        while changed:
            changed = False
            seats = copy.deepcopy(result)
            for i in range(len(seats)):
                for j in range(len(seats[i])):
                    seat = seats[i][j]
                    adjacent = []
                    # Collecting adjacent seat states
                    if i != 0:
                        adjacent += list(s for s in seats[i - 1][max(j - 1, 0):j + 2])
                    if i != len(seats) - 1:
                        adjacent += list(s for s in seats[i + 1][max(j - 1, 0):j + 2])
                    if j != 0:
                        adjacent += list([seats[i][j - 1]])
                    if j != len(seats[i]) - 1:
                        adjacent += list([seats[i][j + 1]])
                    # Applying rules
                    if seat == 'L' and '#' not in adjacent:
                        changed = True
                        result[i][j] = '#'
                    elif seat == '#' and adjacent.count('#') >= 4:
                        changed = True
                        result[i][j] = 'L'
                    else:
                        result[i][j] = seat
        # counting occupied seats and returning it as a string
        return str(sum(row.count('#') for row in result))

    def part2(self) -> str:
        changed = True
        while changed:
            changed = False
            seats = copy.deepcopy(self.entries)
            for i in range(len(seats)):
                for j in range(len(seats[i])):
                    seat = seats[i][j]
                    # Collecting adjacent seats:
                    #
                    # Directions are referenced by points of the compass as below, where * marks the actual seat:
                    #
                    #  NW  N  NE
                    #  W   *   E
                    #  SW  S  SE
                    #
                    # Copy-paste pattern is used here.
                    adjacent = []
                    # NORTH-WEST
                    c = '.'
                    k = 1
                    while c == '.' and i - k >= 0 and j - k >= 0:
                        c = seats[i - k][j - k]
                        k += 1
                    adjacent.append(c)
                    # NORTH
                    c = '.'
                    k = 1
                    while c == '.' and i - k >= 0:
                        c = seats[i - k][j]
                        k += 1
                    adjacent.append(c)
                    # NORTH-EAST
                    c = '.'
                    k = 1
                    while c == '.' and i - k >= 0 and j + k < len(seats[i]):
                        c = seats[i - k][j + k]
                        k += 1
                    adjacent.append(c)
                    # WEST
                    c = '.'
                    k = 1
                    while c == '.' and j - k >= 0:
                        c = seats[i][j - k]
                        k += 1
                    adjacent.append(c)
                    # EAST
                    c = '.'
                    k = 1
                    while c == '.' and j + k < len(seats[i]):
                        c = seats[i][j + k]
                        k += 1
                    adjacent.append(c)
                    # SOUTH-WEST
                    c = '.'
                    k = 1
                    while c == '.' and i + k < len(seats) and j - k >= 0:
                        c = seats[i + k][j - k]
                        k += 1
                    adjacent.append(c)
                    # SOUTH
                    c = '.'
                    k = 1
                    while c == '.' and i + k < len(seats):
                        c = seats[i + k][j]
                        k += 1
                    adjacent.append(c)
                    # SOUTH-EAST
                    c = '.'
                    k = 1
                    while c == '.' and i + k < len(seats) and j + k < len(seats[i]):
                        c = seats[i + k][j + k]
                        k += 1
                    adjacent.append(c)

                    # Applying rules:
                    if seat == 'L' and '#' not in adjacent:
                        changed = True
                        self.entries[i][j] = '#'
                    elif seat == '#' and adjacent.count('#') >= 5:
                        changed = True
                        self.entries[i][j] = 'L'
                    else:
                        self.entries[i][j] = seat
        # counting occupied seats and returning it as a string
        return str(sum(row.count('#') for row in self.entries))
