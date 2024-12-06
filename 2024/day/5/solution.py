from collections import defaultdict
from typing import Dict, List


inline_example = '''47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47'''


def run(input_content: str, part_1: bool, part_2: bool, example: bool, day: str):
    print(f'# Day {day}')
    if not example:
        it = [x.strip() for x in input_content]
    else:
        it = list(x.strip() for x in inline_example.split('\n'))
    row_it = iter(it)
    order = defaultdict(set)
    pages = list()
    for rule in row_it:
        if not rule:
            break
        key, value = rule.split('|')
        order[int(key)].add(int(value))
    pages.extend([int(x) for x in page.split(',')] for page in row_it)

    if part_1:
        print('## Part 1')
        print(sum(page[int(len(page) / 2)] for page in pages if check_ok(order, page)))

    if part_2:
        print('## Part 2')
        print(sum(reorder(order, page) for page in pages if not check_ok(order, page)))


def check_ok(order: Dict[str, str], page: List[List[str]]) -> bool:
    for idx, num in enumerate(page):
        if num in order and any(p in order[num] for p in page[:idx]):
            return False
    return True


def reorder(order:Dict[str, str], page: List[List[str]]) -> int:
    for idx, num in enumerate(page):
        if num in order:
            for i, p in enumerate(page[:idx]):
                if p in order[num]:
                    page[idx], page[i] = page[i], page[idx]
                    return reorder(order, page)
    return page[int(len(page) / 2)]