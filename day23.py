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
    next_steps(0, sy, lines, [], success, part2)

    for s in success:
        l = len(s)
        print(l)
        res = max(l,res)

    return res


def next_steps(x, y, lines, visited, success, part2):
    if x < 0 or x >= len(lines):
        return
    elif y < 0 or y > len(lines[0]):
        return

    c = lines[x][y]

    if x == len(lines) - 1 and c == '.':
        success.append(visited.copy())
        print(len(visited))

    elif (x,y) in visited:
        return

    if c != '#':
        visited.append((x,y))

    if part2:
        if c != '#':
            next_steps(x - 1, y, lines, visited.copy(), success, part2)
            next_steps(x + 1, y, lines, visited.copy(), success, part2)
            next_steps(x, y - 1, lines, visited.copy(), success, part2)
            next_steps(x, y + 1, lines, visited.copy(), success, part2)

    else:
        if c == '.':
            next_steps(x - 1, y, lines, visited.copy(), success, part2)
            next_steps(x + 1, y, lines, visited.copy(), success, part2)
            next_steps(x, y - 1, lines, visited.copy(), success, part2)
            next_steps(x, y + 1, lines, visited.copy(), success, part2)
        elif c == '<':
            next_steps(x, y - 1, lines, visited, success, part2)
        elif c == '>':
            next_steps(x, y + 1, lines, visited, success, part2)
        elif c == '^':
            next_steps(x - 1, y, lines, visited, success, part2)
        elif c == 'v':
            next_steps(x + 1, y, lines, visited, success, part2)


if __name__ == '__main__':
    sys.setrecursionlimit(10000)

    assert day23('day23_test.txt', False) == 94
    assert day23('day23_input.txt', False) == 2238

    assert day23('day23_test.txt', True) == 154
    #assert day23('day23_input.txt', True) == 2238


