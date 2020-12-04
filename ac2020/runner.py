from ac2020.days import AbstractDay


def _get_class(canonical_name: str):
    """
    Gets a class by it's canonical name. Mind that this can only work with classes that does not require
    any argument during instantiation.

    :param canonical_name: the canonical name of the class to load dynamically, e.g. x.y.Module.Class

    :returns: the instance of the class.
    """
    parts = canonical_name.split('.')
    module = ".".join(parts[:-1])
    m = __import__( module )
    for comp in parts[1:]:
        m = getattr(m, comp)
    return type(parts[-1], (m,), {})()


def run(argv):
    """
    Main logic of the program:

     - Requests the number of Day
     - Requests the input
     - Prints the result for Part1
     - Prints the result for Part2
    """
    number_of_day = -1
    while number_of_day < 0:
        data = str(input('Enter # of day (1-24): '))
        if data.isdecimal():
            number_of_day = int(data)
            if number_of_day > 24:
                number_of_day = -1
    day: AbstractDay = _get_class('ac2020.days.Day' + str(number_of_day) + '.Day' + str(number_of_day))
    day.read_input()
    print()
    print('Result for Day' + str(number_of_day) + ':')
    print('Part 1: ' + day.part1())
    print('Part 2: ' + day.part2())

