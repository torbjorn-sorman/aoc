import re

inline_example = '''MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX'''


def run(input_content: str, part_1: bool, part_2: bool, example: bool, day: str):
    print(f'# Day {day}')
    if not example:
        it = [x.strip() for x in input_content]
    else:
        it = list(x.strip() for x in inline_example.split('\n'))
    haystack = [[col for col in x] for x in it]
    if part_1:
        print('## Part 1')
        lines = list(mk_horiz(haystack)) + list(mk_vert(haystack)) + \
            list(mk_diag_f(haystack)) + list(mk_diag_b(haystack))
        print(sum(look(x) for x in lines))

    if part_2:
        print('## Part 2')
        rows = len(haystack)
        cols = len(haystack[0])
        count = 0
        for y in range(1, rows - 1):
            for x in range(1, cols - 1):
                if haystack[y][x] == 'A' and check_x_mas(haystack, y, x):
                    count += 1
        print(count)
        # 1991 is too high


def check_x_mas(h, y, x) -> bool:
    return ((h[y-1][x-1] == 'M' and h[y-1][x+1] == 'S' and h[y+1][x-1] == 'M' and h[y+1][x+1] == 'S') or
            (h[y-1][x-1] == 'M' and h[y-1][x+1] == 'M' and h[y+1][x-1] == 'S' and h[y+1][x+1] == 'S') or
            (h[y-1][x-1] == 'S' and h[y-1][x+1] == 'M' and h[y+1][x-1] == 'S' and h[y+1][x+1] == 'M') or
            (h[y-1][x-1] == 'S' and h[y-1][x+1] == 'S' and h[y+1][x-1] == 'M' and h[y+1][x+1] == 'M'))


def mk_horiz(haystack):
    for row in haystack:
        yield ''.join(row)


def mk_vert(haystack):
    for col in range(len(haystack[0])):
        yield ''.join([row[col] for row in haystack])


def mk_diag_f(haystack):
    rows = len(haystack)
    cols = len(haystack[0])
    for start_col in range(cols - 3):
        yield ''.join(haystack[y][x] for x, y in zip(range(start_col, cols), range(0, rows)))
    for start_row in range(1, rows - 3):
        yield ''.join(haystack[y][x] for x, y in zip(range(0, cols), range(start_row, rows)))


def mk_diag_b(haystack):
    rows = len(haystack)
    cols = len(haystack[0])
    for start_col in range(cols - 3):
        yield ''.join(haystack[y][x] for x, y in zip(range(start_col, cols), range(rows - 1, -1, -1)))
    for start_row in range(rows - 2, 2, -1):
        yield ''.join(haystack[y][x] for x, y in zip(range(0, cols), range(start_row, -1, -1)))


r = re.compile(r'(?=(XMAS))')


def look(row):
    forward = [x for x in r.finditer(row)]
    reverse = [x for x in r.finditer(row[::-1])]
    return len(forward) + len(reverse)
