from typing import List

inline_example = '''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9'''


def try_damp(report: List[int], damp: bool):
    if damp:
        for index in range(len(report)):
            if is_safe([x for idx, x in enumerate(report) if idx != index], False):
                return True
    return False


def is_safe(report: List[int], damp=True) -> bool:
    inc = False
    dec = False
    prev = report[0]
    for v in report[1:]:
        if abs(prev - v) > 3:
            return try_damp(report, damp)
        if prev < v:
            inc = True
            if dec:
                return try_damp(report, damp)
        elif prev > v:
            dec = True
            if inc:
                return try_damp(report, damp)
        else:
            return try_damp(report, damp)
        prev = v
    return True


def run(input_content: str, part_1: bool, part_2: bool, example: bool, day: str):
    print(f'# Day {day}')
    if not example:
        it = [x.strip() for x in input_content]
    else:
        it = list(x.strip() for x in inline_example.split('\n'))
    reports = [[int(y) for y in x.split()] for x in it]
    if part_1:
        print('## Part 1')
        print(len([x for x in reports if is_safe(x, False)]))

    if part_2:
        print('## Part 2')
        print(len([x for x in reports if is_safe(x)]))
