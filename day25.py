from operator import itemgetter


def day25(filename, part2):
    print('Day 25: Snowverload')

    res = 0
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
        res = solve(lines, part2)
        print(res)

    return res


def solve(lines, part2):
    res = 0

    input = {}

    for line in lines:
        head,tail = line.split(":")
        t = tail.split(" ")
        input[head] = t

    return res



if __name__ == '__main__':
    assert day25('day25_test.txt', False) == 5


