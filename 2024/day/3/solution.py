import re

inline_example = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
inline_example2 = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""


def run(input_content: str, part_1: bool, part_2: bool, example: bool, day: str):
    print(f'# Day {day}')
    if not example:
        it = [x.strip() for x in input_content]
    else:
        it = [inline_example.strip()]
    if part_1:
        print('## Part 1')
        r = re.compile(r'(mul\(\d\d?\d?,\d\d?\d?\))')
        res = 0
        for y in it:
            for m in r.findall(y):
                x, y = m[4:-1].split(',')
                res += int(x) * int(y)
        print(res)
    if part_2:
        print('## Part 2')
        r = re.compile(r"(mul\(\d\d?\d?,\d\d?\d?\)|do\(\)|don't\(\))")
        res = 0
        if example:
            it = [inline_example2]
        go = True
        for y in it:
            for m in r.findall(y):
                if m == 'do()':
                    go = True
                elif m == "don't()":
                    go = False
                else:
                    if go:
                        x, y = m[4:-1].split(',')
                        res += int(x) * int(y)
        print(res)
