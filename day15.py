
def day15(filename):
    print('Day 15: Lens Library')

    res = 0
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
        res = solve(lines)
        print(res)

    return res


def solve(lines):
    res = 0

    values = lines[0].split(',')

    for value in values:
        cv = 0
        for c in value:
            ascii = ord(c)
            cv += ascii
            cv = cv*17
            cv = cv%256
        print(value, cv)
        res += cv
    return res


if __name__ == '__main__':
    assert day15('day15_test.txt') == 1320
    assert day15('day15_input.txt') == 501680


