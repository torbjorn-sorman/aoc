inline_example = '''89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732'''


def run(input_content: str, part_1: bool, part_2: bool, example: bool, day: str):
    print(f'# Day {day}')
    if not example:
        it = [x.strip() for x in input_content]
    else:
        it = list(x.strip() for x in inline_example.split('\n'))
    pad_rows = [[-1]*(len(it[0]) + 2)]
    world = [[-1, *[int(x) for x in y], -1] for y in pad_rows + it + pad_rows]
    heads = list()
    for y, row in enumerate(world):
        for x, col in enumerate(row):
            if col == 0:
                heads.append((x, y))
    if part_1:
        print('## Part 1')
        print(sum(count_trails(world, *head) for head in heads))
    if part_2:
        print('## Part 2')
        print(sum(check_rating(world, *head) for head in heads))


def count_trails(world, x, y):
    trails = set()
    impl(world, x, y, trails)
    return len(trails)


def impl(world, x, y, trails):
    if world[y][x] == 9:
        trails.add((x, y))
    else:
        if world[y][x + 1] - world[y][x] == 1:
            impl(world, x+1, y, trails)
        if world[y][x - 1]-world[y][x] == 1:
            impl(world, x-1, y, trails)
        if world[y+1][x] - world[y][x] == 1:
            impl(world, x, y+1, trails)
        if world[y-1][x]-world[y][x] == 1:
            impl(world, x, y-1, trails)


def check_rating(world, x, y):
    trails = set()
    impl_rating(world, [(x, y)], trails)
    return len(trails)


def impl_rating(world, path, trails):
    x, y = path[-1]
    if world[y][x] == 9:
        trails.add(tuple(path))
    else:
        if world[y][x + 1] - world[y][x] == 1:
            impl_rating(world, path + [(x+1, y)], trails)
        if world[y][x - 1]-world[y][x] == 1:
            impl_rating(world, path + [(x-1, y)], trails)
        if world[y+1][x] - world[y][x] == 1:
            impl_rating(world, path + [(x, y+1)], trails)
        if world[y-1][x]-world[y][x] == 1:
            impl_rating(world, path + [(x, y-1)], trails)
