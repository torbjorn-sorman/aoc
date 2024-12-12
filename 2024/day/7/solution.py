import itertools


inline_example = '''190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20'''


def run(input_content: str, part_1: bool, part_2: bool, example: bool, day: str):
    print(f'# Day {day}')
    if not example:
        it = [x.strip() for x in input_content]
    else:
        it = list(x.strip() for x in inline_example.split('\n'))
    if part_1:
        print('## Part 1')
        s = 0
        for eq in it:
            result, input = eq.split(':')
            s += do_test(int(result), [int(x) for x in input.split()], (0, 1))
        print(s)
    if part_2:
        print('## Part 2')
        s = 0
        for eq in it:
            result, input = eq.split(':')
            s += do_test(int(result), [int(x)
                         for x in input.split()], (0, 1, 2))
        print(s)


def do_test(result: int, inputs: list, rng):
    for op in itertools.product(rng, repeat=len(inputs) - 1):
        test = list(_mk(op, inputs))
        if _apply(test) == result:
            return result
    return 0


def _apply(xs):
    it = iter(xs)
    result = next(it)
    try:
        while True:
            _y = next(it)
            if _y == 0:
                result = result + next(it)
            elif _y == 1:
                result = result * next(it)
            elif _y == 2:
                result = int(str(result) + str(next(it)))
    except:
        pass
    return result


def _mk(ops, inp):
    o_it = iter(ops)
    for x in inp[:-1]:
        yield x
        yield next(o_it)
    yield inp[-1]
