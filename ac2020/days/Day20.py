from copy import deepcopy
from math import prod, sqrt

from ac2020.days import AbstractDay
from ac2020.io import InputReader


def get_border(tile, side):
    """
    Gets the border of a tile.

    Side codes:
     - 0: top
     - 1: right
     - 2: bottom
     - 3: left

    :return: the line or column at the and of a tile based on the give side configuration.
    """
    if side == 0:
        return ''.join(tile[0])
    if side == 1:
        return ''.join([x[-1] for x in tile])
    if side == 2:
        return ''.join(tile[-1])
    if side == 3:
        return ''.join([x[0] for x in tile])
    return ''


def flip_tile_x(tile):
    """
    Flips a tile horizontally
    """
    return [x[::-1] for x in tile]


def flip_tile_y(tile):
    """
    Flips a tile vertically
    """
    return tile[::-1]


def rotate_right(tile):
    """
    Rotates a tile by 90 degrees clockwise
    """
    return [list(x) for x in zip(*tile[::-1])]


def print_tile(tile):
    """
    Prints a tile to std. out. Basically a debug tool.
    """
    for row in tile:
        print(''.join(row))
    print()


class Day20(AbstractDay.AbstractDay):
    """
    Advent of Code 2020 - Day 20
    ============================

    The high-speed train leaves the forest and quickly carries you south. You can even see a desert in
    the distance! Since you have some spare time, you might as well see if there was anything interesting in
    the image the Mythical Information Bureau satellite captured.

    After decoding the satellite messages, you discover that the data actually contains many small
    images created by the satellite's camera array. The camera array consists of many cameras; rather than
    produce a single square image, they produce many smaller square image tiles that need to be
    reassembled back into a single image.

    Each camera in the camera array returns a single monochrome image tile with a random unique ID number.
    The tiles (your puzzle input) arrived in a random order.

    Worse yet, the camera array appears to be malfunctioning: each image tile has been rotated and
    flipped to a random orientation. Your first task is to reassemble the original image by orienting
    the tiles so they fit together.

    To show how the tiles should be reassembled, each tile's image data includes a border that
    should line up exactly with its adjacent tiles. All tiles have this border, and the border lines up
    exactly when the tiles are both oriented correctly. Tiles at the edge of the image also
    have this border, but the outermost edges won't line up with any other tiles.

    For example, suppose you have the following nine tiles:

    Tile 2311:
    ..##.#..#.
    ##..#.....
    #...##..#.
    ####.#...#
    ##.##.###.
    ##...#.###
    .#.#.#..##
    ..#....#..
    ###...#.#.
    ..###..###

    Tile 1951:
    #.##...##.
    #.####...#
    .....#..##
    #...######
    .##.#....#
    .###.#####
    ###.##.##.
    .###....#.
    ..#.#..#.#
    #...##.#..

    Tile 1171:
    ####...##.
    #..##.#..#
    ##.#..#.#.
    .###.####.
    ..###.####
    .##....##.
    .#...####.
    #.##.####.
    ####..#...
    .....##...

    Tile 1427:
    ###.##.#..
    .#..#.##..
    .#.##.#..#
    #.#.#.##.#
    ....#...##
    ...##..##.
    ...#.#####
    .#.####.#.
    ..#..###.#
    ..##.#..#.

    Tile 1489:
    ##.#.#....
    ..##...#..
    .##..##...
    ..#...#...
    #####...#.
    #..#.#.#.#
    ...#.#.#..
    ##.#...##.
    ..##.##.##
    ###.##.#..

    Tile 2473:
    #....####.
    #..#.##...
    #.##..#...
    ######.#.#
    .#...#.#.#
    .#########
    .###.#..#.
    ########.#
    ##...##.#.
    ..###.#.#.

    Tile 2971:
    ..#.#....#
    #...###...
    #.#.###...
    ##.##..#..
    .#####..##
    .#..####.#
    #..#.#..#.
    ..####.###
    ..#.#.###.
    ...#.#.#.#

    Tile 2729:
    ...#.#.#.#
    ####.#....
    ..#.#.....
    ....#..#.#
    .##..##.#.
    .#.####...
    ####.#.#..
    ##.####...
    ##..#.##..
    #.##...##.

    Tile 3079:
    #.#.#####.
    .#..######
    ..#.......
    ######....
    ####.#..#.
    .#...#.##.
    #.#####.##
    ..#.###...
    ..#.......
    ..#.###...

    By rotating, flipping, and rearranging them, you can find a square arrangement that
    causes all adjacent borders to line up:

    #...##.#.. ..###..### #.#.#####.
    ..#.#..#.# ###...#.#. .#..######
    .###....#. ..#....#.. ..#.......
    ###.##.##. .#.#.#..## ######....
    .###.##### ##...#.### ####.#..#.
    .##.#....# ##.##.###. .#...#.##.
    #...###### ####.#...# #.#####.##
    .....#..## #...##..#. ..#.###...
    #.####...# ##..#..... ..#.......
    #.##...##. ..##.#..#. ..#.###...

    #.##...##. ..##.#..#. ..#.###...
    ##..#.##.. ..#..###.# ##.##....#
    ##.####... .#.####.#. ..#.###..#
    ####.#.#.. ...#.##### ###.#..###
    .#.####... ...##..##. .######.##
    .##..##.#. ....#...## #.#.#.#...
    ....#..#.# #.#.#.##.# #.###.###.
    ..#.#..... .#.##.#..# #.###.##..
    ####.#.... .#..#.##.. .######...
    ...#.#.#.# ###.##.#.. .##...####

    ...#.#.#.# ###.##.#.. .##...####
    ..#.#.###. ..##.##.## #..#.##..#
    ..####.### ##.#...##. .#.#..#.##
    #..#.#..#. ...#.#.#.. .####.###.
    .#..####.# #..#.#.#.# ####.###..
    .#####..## #####...#. .##....##.
    ##.##..#.. ..#...#... .####...#.
    #.#.###... .##..##... .####.##.#
    #...###... ..##...#.. ...#..####
    ..#.#....# ##.#.#.... ...##.....
    For reference, the IDs of the above tiles are:

    1951    2311    3079
    2729    1427    2473
    2971    1489    1171
    To check that you've assembled the image correctly, multiply the IDs of the four corner tiles together.
    If you do this with the assembled tiles from the example above, you get 1951 * 3079 * 2971 * 1171 = 20899048083289.

    Assemble the tiles into an image. What do you get if you multiply together the IDs of the four corner tiles?

    --- Part Two ---
    ----------------

    Now, you're ready to check the image for sea monsters.

    The borders of each tile are not part of the actual image; start by removing them.

    In the example above, the tiles become:

    .#.#..#. ##...#.# #..#####
    ###....# .#....#. .#......
    ##.##.## #.#.#..# #####...
    ###.#### #...#.## ###.#..#
    ##.#.... #.##.### #...#.##
    ...##### ###.#... .#####.#
    ....#..# ...##..# .#.###..
    .####... #..#.... .#......

    #..#.##. .#..###. #.##....
    #.####.. #.####.# .#.###..
    ###.#.#. ..#.#### ##.#..##
    #.####.. ..##..## ######.#
    ##..##.# ...#...# .#.#.#..
    ...#..#. .#.#.##. .###.###
    .#.#.... #.##.#.. .###.##.
    ###.#... #..#.##. ######..

    .#.#.### .##.##.# ..#.##..
    .####.## #.#...## #.#..#.#
    ..#.#..# ..#.#.#. ####.###
    #..####. ..#.#.#. ###.###.
    #####..# ####...# ##....##
    #.##..#. .#...#.. ####...#
    .#.###.. ##..##.. ####.##.
    ...###.. .##...#. ..#..###
    Remove the gaps to form the actual image:

    .#.#..#.##...#.##..#####
    ###....#.#....#..#......
    ##.##.###.#.#..######...
    ###.#####...#.#####.#..#
    ##.#....#.##.####...#.##
    ...########.#....#####.#
    ....#..#...##..#.#.###..
    .####...#..#.....#......
    #..#.##..#..###.#.##....
    #.####..#.####.#.#.###..
    ###.#.#...#.######.#..##
    #.####....##..########.#
    ##..##.#...#...#.#.#.#..
    ...#..#..#.#.##..###.###
    .#.#....#.##.#...###.##.
    ###.#...#..#.##.######..
    .#.#.###.##.##.#..#.##..
    .####.###.#...###.#..#.#
    ..#.#..#..#.#.#.####.###
    #..####...#.#.#.###.###.
    #####..#####...###....##
    #.##..#..#...#..####...#
    .#.###..##..##..####.##.
    ...###...##...#...#..###

    Now, you're ready to search for sea monsters! Because your image is monochrome, a sea monster will look like this:

                      #
    #    ##    ##    ###
     #  #  #  #  #  #

    When looking for this pattern in the image, the spaces can be anything; only the # need to match.
    Also, you might need to rotate or flip your image before it's oriented correctly to find sea monsters.
    In the above image, after flipping and rotating it to the appropriate orientation,
    there are two sea monsters (marked with O):

    .####...#####..#...###..
    #####..#..#.#.####..#.#.
    .#.#...#.###...#.##.O#..
    #.O.##.OO#.#.OO.##.OOO##
    ..#O.#O#.O##O..O.#O##.##
    ...#.#..##.##...#..#..##
    #.##.#..#.#..#..##.#.#..
    .###.##.....#...###.#...
    #.####.#.#....##.#..#.#.
    ##...#..#....#..#...####
    ..#.##...###..#.#####..#
    ....#.##.#.#####....#...
    ..##.##.###.....#.##..#.
    #...#...###..####....##.
    .#.##...#.##.#.#.###...#
    #.###.#..####...##..#...
    #.###...#.##...#.##O###.
    .O##.#OO.###OO##..OOO##.
    ..O#.O..O..O.#O##O##.###
    #.#..##.########..#..##.
    #.#####..#.#...##..#....
    #....##..#.#########..##
    #...#.....#..##...###.##
    #..###....##.#...##.##.#

    Determine how rough the waters are in the sea monsters' habitat by counting the number of # that
    are not part of a sea monster. In the above example, the habitat's water roughness is 273.

    How many # are not part of a sea monster?
    """

    def _set_input(self, input_: str):
        self.entries = {}
        self.corners = []
        self.neighbors = {}
        if len(input_) != 0:
            tiles = input_.split('\n\n')
            for tile in tiles:
                split = tile.split('\n', 1)
                id_ = int(split[0].replace('Tile ', '').replace(':', ''))
                image = InputReader.read_character_matrix(split[1])
                self.entries[id_] = image

    def part1(self) -> str:
        """
        Just finding the four corners to check Part2 for further details
        """
        if len(self.entries) == 0:
            return 'No result'
        for id_ in self.entries:
            matching_sides = 0
            tile = self.entries[id_]
            self.neighbors[id_] = []
            for other_id_ in self.entries:
                if other_id_ == id_:
                    continue
                other = self.entries[other_id_]
                for i in range(4):
                    for j in range(4):
                        border_a = get_border(tile, i)
                        border_b = get_border(other, j)
                        if border_a == border_b or\
                           border_a[::-1] == border_b or\
                           border_a == border_b[::-1] or \
                           border_a[::-1] == border_b[::-1]:
                            matching_sides += 1
                            self.neighbors[id_].append(other_id_)
            if matching_sides == 2:
                self.corners.append(id_)
        return str(prod(self.corners))

    def part2(self) -> str:
        """
        I'm definitely not proud of this. It works, but that's all, strongly relies on the Copy-Paste pattern.
        """
        if len(self.entries) == 0:
            return 'No result'
        dim = int(sqrt(len(self.entries)))
        tiled = []
        for i in range(dim):
            tiled.append([0] * dim)
        corner = self.corners[0]
        good = 0
        # Orienting the first corner tile so that the borders with neighbors are getting to the correct position.
        tries = 0
        while good != 2:
            good = 0
            neighbor = self.neighbors[corner][0]
            border_a = get_border(self.entries[corner], 1)
            for i in range(4):
                border_b = get_border(self.entries[neighbor], i)
                if border_a == border_b or border_a == border_b[::-1]:
                    good += 1
                    neighbor = self.neighbors[corner][1]
                    break
            border_a = get_border(self.entries[corner], 2)
            for i in range(4):
                border_b = get_border(self.entries[neighbor], i)
                if border_a == border_b or border_a == border_b[::-1]:
                    good += 1
                    break
            if good == 2:
                break
            tries += 1
            if tries % 4 != 0:
                self.entries[corner] = rotate_right(self.entries[corner])
            elif tries % 8 == 0:
                self.entries[corner] = flip_tile_x(self.entries[corner])
            elif tries % 4 == 0:
                self.entries[corner] = flip_tile_y(self.entries[corner])
        # Tileing configuration is being calculated. First in position is the first corner.
        # All the next tiles are placed by tiles already in the configuration by rotating and flipping the
        # next one to connect to the last one.
        tiled[0][0] = corner
        for i in range(dim):
            for j in range(dim - 1):
                if tiled[i][j + 1] == 0:
                    border_a = get_border(self.entries[tiled[i][j]], 1)
                    hit = None
                    for neighbor in self.neighbors[tiled[i][j]]:
                        for k in range(4):
                            border_b = get_border(self.entries[neighbor], k)
                            if border_a == border_b or border_a == border_b[::-1]:
                                good += 1
                                hit = neighbor
                                break
                    tries = 0
                    while border_a != get_border(self.entries[hit], 3):
                        if tries % 4 != 0:
                            self.entries[hit] = rotate_right(self.entries[hit])
                        elif tries % 8 == 0:
                            self.entries[hit] = flip_tile_x(self.entries[hit])
                        elif tries % 4 == 0:
                            self.entries[hit] = flip_tile_y(self.entries[hit])
                        tries += 1
                    tiled[i][j + 1] = hit
                if i != dim - 1 and tiled[i + 1][j] == 0:
                    border_a = get_border(self.entries[tiled[i][j]], 2)
                    hit = None
                    for neighbor in self.neighbors[tiled[i][j]]:
                        for k in range(4):
                            border_b = get_border(self.entries[neighbor], k)
                            if border_a == border_b or border_a == border_b[::-1]:
                                good += 1
                                hit = neighbor
                                break
                    tries = 0
                    while get_border(self.entries[tiled[i][j]], 2) != get_border(self.entries[hit], 0):
                        if tries % 4 != 0:
                            self.entries[hit] = rotate_right(self.entries[hit])
                        elif tries % 8 == 0:
                            self.entries[hit] = flip_tile_x(self.entries[hit])
                        elif tries % 4 == 0:
                            self.entries[hit] = flip_tile_y(self.entries[hit])
                        tries += 1
                    tiled[i + 1][j] = hit

        # Rendering the tiled image.
        image = ''
        for i in range(dim):
            for j in range(1, 9):
                for k in range(dim):
                    image += ''.join(self.entries[tiled[i][k]][j][1:-1])
                image += '\n'
        image = image.strip()

        # Searching for monsters.
        monster = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                   [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1],
                   [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0]]

        target = InputReader.read_character_matrix(image)
        maxi_arrangement = []
        maxi = 0
        tries = 0
        # Each iteration finds the monster, then stores if this is the best solution yet (marked image is also stored)
        # Then flippidy-floppidy-rotating the image for the next iteration.
        # 12 iterations are performed, because there are 4 rotates for each flippidy and floppidy and of course
        # the non-flippidy-floppidied version.
        while tries < 12:
            hit_count = 0
            marked_target = deepcopy(target)
            for i in range(len(target)-3):
                for j in range(len(target[0])-20):
                    hit = True
                    for im in range(3):
                        for jm in range(20):
                            if monster[im][jm] != 0 and target[i + im][j + jm] != '#':
                                hit = False
                    if hit:
                        hit_count += 1
                        for im in range(3):
                            for jm in range(20):
                                if monster[im][jm] != 0:
                                    marked_target[i + im][j + jm] = 'O'
            if hit_count >= maxi:
                maxi = hit_count
                maxi_arrangement = marked_target

            if tries % 4 != 0:
                target = rotate_right(target)
            elif tries != 0 and tries % 8 == 0:
                target = flip_tile_x(target)
            elif tries != 0 and tries % 4 == 0:
                target = flip_tile_y(target)
            tries += 1
        # Providing the result
        return str(sum([x.count('#') for x in maxi_arrangement]))
