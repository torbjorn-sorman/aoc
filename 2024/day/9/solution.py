import re


inline_example = '''2333133121414131402'''


def run(input_content: str, part_1: bool, part_2: bool, example: bool, day: str):
    print(f'# Day {day}')
    if not example:
        it = [x.strip() for x in input_content]
    else:
        it = list(x.strip() for x in inline_example.split('\n'))
    file_length = dict()
    disc = get_disc(it, file_length)
    if part_1:
        print('## Part 1')
        start = 0
        for i in range(len(disc) - 1, -1, -1):
            if disc[i] > -1:
                for left in range(start, i):
                    if disc[left] < 0:
                        disc[left], disc[i] = disc[i], disc[left]
                        start = left + 1
                        break
        print(sum(idx * x for idx, x in enumerate(disc) if x > -1))
    if part_2:
        print('## Part 2')
        i = len(disc) - 1
        while i > 0:
            if disc[i] > -1:
                n = file_length[disc[i]]
                for left in range(0, i):
                    if disc[left] < 0 and abs(disc[left]) >= n:
                        for j in range(n):
                            disc[left + j], disc[i - j] = disc[i - j], disc[left + j]
                        break
                i -= n
            else:
                i -= 1
        print(sum(idx * x for idx, x in enumerate(disc) if x > -1))


def get_disc(it, file_length):
    seq = it[0]
    disc = list()
    all_pairs = re.findall('..', seq)
    for idx, [f, e] in enumerate(all_pairs):
        disc.extend([idx] * int(f))
        disc.extend(x for x in range(-int(e), 0))
        file_length[idx] = int(f)
    if len(seq) % 2 != 0:
        disc.extend([len(all_pairs)] * int(seq[-1]))
        file_length[len(all_pairs)] = int(seq[-1])
    return disc
