import collections
import itertools


inline_example = '''............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............'''


def run(input_content: str, part_1: bool, part_2: bool, example: bool, day: str):
    print(f'# Day {day}')
    if not example:
        it = [x.strip() for x in input_content]
    else:
        it = list(x.strip() for x in inline_example.split('\n'))
    world = [[x for x in y] for y in it]
    rows = len(world)
    cols = len(world[0])
    freqs = collections.defaultdict(set)
    for y, row in enumerate(world):
        for x, val in enumerate(row):
            if val != '.':
                freqs[val].add((x, y))
    if part_1:
        print('## Part 1')
        antinodes = set()
        for freq, ants in freqs.items():
            for a1, a2 in list(itertools.combinations(ants, 2)):
                antinodes.update(x for x in mk_antinode(
                    *a1, *a2) if 0 <= x[0] < cols and 0 <= x[1] < rows)
        print(len(antinodes))

    if part_2:
        print('## Part 2')
        antinodes = set()
        for freq, ants in freqs.items():
            for a1, a2 in list(itertools.combinations(ants, 2)):
                antinodes.update(
                    x for x in mk_antinode_harm(
                        *a1, *a2, max(cols, rows)) if 0 <= x[0] < cols and 0 <= x[1] < rows)
        for y, row in enumerate(world):
            line = ''
            for x, val in enumerate(row):
                if (x, y) in antinodes:
                    line += '#'
                else:
                    line += val
            # print(line)
        print(len(antinodes))


def mk_antinode(x1, y1, x2, y2):
    yield x1 + x1 - x2, y1 + y1 - y2
    yield x2 + x2 - x1, y2 + y2 - y1


def mk_antinode_harm(x1, y1, x2, y2, lim):
    d1x = x1 - x2
    d1y = y1 - y2
    d2x = x2 - x1
    d2y = y2 - y1
    yield x1, y1
    yield x2, y2
    yield from ((x1 + d1x * i, y1 + d1y * i) for i in range(lim))
    yield from ((x2 + d2x * i, y2 + d2y * i) for i in range(lim))
