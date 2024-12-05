import math
import collections

inline_example = '''3   4
4   3
2   5
1   3
3   9
3   3'''


def run(input_content: str, part_1: bool, part_2: bool, example: bool, day: str):
    print(f'# Day {day}')
    if not example:
        it = [x.strip() for x in input_content]
    else:
        it = list(x.strip() for x in inline_example.split('\n'))
    left_list = list()
    right_list = list()
    for left, right in ((x.split() for x in it)):
        left_list.append(int(left))
        right_list.append(int(right))
    if part_1:
        print('## Part 1')
        left_list.sort()
        right_list.sort()
        dist = list()
        for left, right in zip(left_list, right_list):
            dist.append(abs(int(left) - int(right)))
        print(sum(dist))
    if part_2:
        print('## Part 2')
        c = collections.Counter(right_list)
        print(sum(x * c[x] for x in left_list))
