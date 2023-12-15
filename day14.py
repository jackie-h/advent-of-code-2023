
def day14(filename):
    print('Day 14: Parabolic Reflector Dish')

    res = 0
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
        res = solve(lines)
        print(res)

    return res


def solve(lines):
    res = 0

    height = len(lines)
    res = [[]]*len(lines[0])
    vals = [height]*len(lines[0])
    for x,line in enumerate(lines):
        for y,c in enumerate(line):
            if c == 'O':
                val = vals[y]
                vals[y] = vals[y] - 1
                res[y].append(val)
                print((x,y),val)
            elif c == '#':
                vals[y] = height - x - 1
    total = 0
    for r in res:
        total += sum(r)
    return total


if __name__ == '__main__':
    assert day14('day14_test.txt') == 136
    assert day14('day14_input.txt') == 103333

