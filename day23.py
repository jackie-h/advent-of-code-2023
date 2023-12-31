import sys


def day23(filename, part2):
    print('Day 23: A Long Walk')

    res = 0
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
        res = solve(lines, part2)
        print(res)

    return res


def solve(lines, part2):
    res = 0

    sy = lines[0].find('.')

    success = []
    next_steps(0, sy, lines, [], success)

    for s in success:
        l = len(s)
        print(l)
        res = max(l,res)

    return res


def next_steps(x, y, lines, visited, success):
    if x < 0 or x >= len(lines):
        return
    elif y < 0 or y > len(lines[0]):
        return

    c = lines[x][y]

    if x == len(lines) - 1 and c == '.':
        success.append(visited.copy())

    elif (x,y) in visited:
        return

    if c != '#':
        visited.append((x,y))

    if c == '.':
        next_steps(x - 1, y, lines, visited.copy(), success)
        next_steps(x + 1, y, lines, visited.copy(), success)
        next_steps(x, y - 1, lines, visited.copy(), success)
        next_steps(x, y + 1, lines, visited.copy(), success)
    elif c == '<':
        next_steps(x, y - 1, lines, visited, success)
    elif c == '>':
        next_steps(x, y + 1, lines, visited, success)
    elif c == '^':
        next_steps(x - 1, y, lines, visited, success)
    elif c == 'v':
        next_steps(x + 1, y, lines, visited, success)


if __name__ == '__main__':
    sys.setrecursionlimit(10000)

    assert day23('day23_test.txt', False) == 94
    assert day23('day23_input.txt', False) == 2238


