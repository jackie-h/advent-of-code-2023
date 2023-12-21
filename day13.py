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
        row_mirrors = []
        find_mirror(row_mirrors, puzzle)

        flipped = ['']*len(puzzle[0])
        for i in range(0,len(puzzle)):
            for j in range(0,len(puzzle[0])):
                flipped[j] += puzzle[i][j]

        column_mirrors = []
        find_mirror(column_mirrors, flipped)

        puzzle_res = sum(row_mirrors) * 100 + sum(column_mirrors)
        res += puzzle_res
        print(row_mirrors,column_mirrors,puzzle_res)


    return res


def find_mirror(mirrors, puzzle):
    for i, line in enumerate(puzzle):
        if i < len(puzzle) - 1 and line == puzzle[i + 1]:
            d = 1
            is_mirror = True
            while is_mirror and i - d >= 0 and i + 1 + d < len(puzzle):
                a = puzzle[i - d]
                b = puzzle[i + 1 + d]
                is_mirror = a == b
                d += 1

            if is_mirror:
                mirrors.append(i + 1)


if __name__ == '__main__':
    assert day13('day13_test.txt', False) == 405
    assert day13('day13_input.txt', False) == 31739
