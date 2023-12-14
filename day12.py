from itertools import combinations


def day12(filename):
    print('Day 12: Hot Springs')

    res = 0
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
        res = solve(lines)
        print(res)

    return res


def solve(lines):
    res = 0
    for line in lines:
        print(line)
        row,tail = line.split()
        values = list(map(int, tail.split(',')))
        groups = len(values)
        n_empty = len(row) - sum(values)
        max_adj_empty = n_empty - (len(values) - 1)


        possibles = []
        for p in combinations(range(groups + n_empty), groups):
            # for i,v in enumerate(p):
            #     if [i]

            print(p)


    return res


if __name__ == '__main__':

    assert day12('day12_test.txt') == 374

