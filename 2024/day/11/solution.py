import math


inline_example = '''125 17'''


def run(input_content: str, part_1: bool, part_2: bool, example: bool, day: str):
    print(f'# Day {day}')
    if not example:
        it = [x.strip() for x in input_content]
    else:
        it = list(x.strip() for x in inline_example.split('\n'))
    stones = [int(x) for x in it[0].split()]
    if part_1:
        print('## Part 1')
        mem = dict()
        print(sum(blink_all(mem, x, 0) for x in stones))
    if part_2:
        print('## Part 2')
        mem = dict()
        print(sum(blink_all(mem, x, 0, target=75) for x in stones))


def blink_all(mem, stone, depth, target=25):
    if depth + 1 == target:
        return len(blink(stone))
    key = (depth, stone)
    if key not in mem:
        mem[key] = sum(blink_all(mem, x, depth + 1, target)
                       for x in blink(stone))
    return mem[key]


def blink(x: int):
    if x == 0:
        return [1]
    n = int(math.log(x, 10) + 1)
    if n % 2 == 0:
        d = int(math.pow(10, n / 2))
        a = int(x / d)
        b = x - a * d
        return [a, b]
    return [x * 2024]
