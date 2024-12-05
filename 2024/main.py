#!/usr/bin/env python

import argparse
import importlib
import os
import pathlib
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('days', nargs='+')
    parser.add_argument('-p1', '--part_1', action='store_true', default=False)
    parser.add_argument('-p2', '--part_2', action='store_true', default=False)
    parser.add_argument('-e', '--example', action='store_true', default=False)
    args = parser.parse_args()
    [download_input_and_load_module(
        2024, day, args.part_1, args.part_2, args.example) for day in args.days]


def download_input_and_load_module(year: int, day: str, part_1: bool, part_2: bool, example: bool):
    mt = importlib.import_module(f'day.{day}.solution')
    dst = os.path.join(pathlib.Path(
        __file__).parent.resolve(), 'day', day, 'input.txt')
    src = f'https://adventofcode.com/{year}/day/{day}/input.txt'
    if not os.path.exists(dst):
        print(f'Download input from {src}')
        sys.exit(1)
    if not part_1 and not part_2:
        part_1 = True
        part_2 = True
    with open(dst, 'r') as f:
        input_content = [x.strip() for x in f]
    getattr(mt, 'run')(input_content, part_1, part_2, example, day)


if __name__ == "__main__":
    main()
