import collections


def day17(filename, part2):
    print('Day 17: Clumsy Crucible')

    res = 0
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
        res = solve(lines, part2)
        print(res)

    return res


def solve(lines, part2):
    res = 0

    start = (0,0)

    q = collections.deque()
    q.append(start)

    #while len(q) > 0:





    return res


if __name__ == '__main__':
    assert day17('day17_test.txt', False) == 102
