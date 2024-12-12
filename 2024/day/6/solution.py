import copy


inline_example = '''....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...'''


class Guard:
    y: int
    x: int
    dir: str


def run(input_content: str, part_1: bool, part_2: bool, example: bool, day: str):
    print(f'# Day {day}')
    if not example:
        it = [x.strip() for x in input_content]
    else:
        it = list(x.strip() for x in inline_example.split('\n'))
    world = [[x for x in y] for y in it]
    guard = Guard()
    for row, y in enumerate(it):
        for col, x in enumerate(y):
            if x != '.' and x != '#':
                guard.y = row
                guard.x = col
                guard.dir = x
    world[guard.y][guard.x] = '.'
    if part_1:
        print('## Part 1')
        visit = set()
        while within(world, guard.x, guard.y):
            visit.add((guard.y, guard.x))
            if step_out(world, guard):
                break
        print(len(visit))
    if part_2:
        print('## Part 2')
        print(part_try_all(world, guard))


def part_try_all(world, guard):
    no_go = guard.x, guard.y
    loops = 0
    for y, row in enumerate(world):
        for x, val in enumerate(row):
            if val == '.' and (x, y) != no_go:
                s = world[y][x]
                world[y][x] = '#'
                if is_in_loop(world, copy.deepcopy(guard)):
                    loops += 1
                world[y][x] = s
    return loops


def is_in_loop(world, g):
    visit = set()
    while True:
        key = (g.y, g.x, g.dir)
        if key in visit:
            return True
        visit.add(key)
        if step_out(world, g):
            return False


def step_out(world, g):
    match g.dir:
        case '^':
            if not within(world, g.x, g.y-1):
                return True
            if world[g.y - 1][g.x] == '.':
                g.y -= 1
            else:
                g.dir = '>'
        case '>':
            if not within(world, g.x + 1, g.y):
                return True
            if world[g.y][g.x + 1] == '.':
                g.x += 1
            else:
                g.dir = 'v'
        case 'v':
            if not within(world, g.x, g.y+1):
                return True
            if world[g.y + 1][g.x] == '.':
                g.y += 1
            else:
                g.dir = '<'
        case '<':
            if not within(world, g.x-1, g.y):
                return True
            if world[g.y][g.x - 1] == '.':
                g.x -= 1
            else:
                g.dir = '^'
    return False


def within(world, x, y):
    rows = len(world)
    cols = len(world[0])
    return y >= 0 and y < rows and x >= 0 and x < cols
