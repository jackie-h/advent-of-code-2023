import collections


def day13(filename, part2):
    print('Day 13: Point of Incidence')

    res = 0
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
        res = solve(lines, part2)
        print(res)

    return res


def solve(lines, part2):
    res = 0

    puzzle = 0
    puzzles = [[]]
    for line in lines:
        if line == '':
            puzzle += 1
            puzzles.append([])
        else:
            puzzles[puzzle].append(line)

    for puzzle in puzzles:
        mirrors = []
        for i,line in enumerate(puzzle):
            if i < len(puzzle) - 1 and line == puzzle[i+1]:
                d = 1
                is_mirror = True
                while is_mirror and i-d > 0 and i+1+d < len(puzzle):
                    is_mirror = puzzle[i-d] == puzzle[i+1+d]
                    d += 1

                if is_mirror:
                    mirrors.append(i + 1)

        res += sum(mirrors) * 100
        print(mirrors)


    return res


if __name__ == '__main__':
    assert day13('day13_test.txt', False) == 405
