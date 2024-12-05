inline_example = ''''''

def run(input_content: str, part_1: bool, part_2: bool, example: bool, day: str):
    print(f'# Day {day}')
    if not example:
        it = [x.strip() for x in input_content]
    else:
        it = list(x.strip() for x in inline_example.split('\n'))
    if part_1:
        print('## Part 1')
    if part_2:
        print('## Part 2')
