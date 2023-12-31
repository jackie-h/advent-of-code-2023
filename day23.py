import collections
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
    paths = collections.deque()
    paths.append((0,sy,[]))
    next_steps(paths, lines, success, part2)

    for s in success:
        l = len(s)
        print(l)
        res = max(l,res)

    return res


def next_steps(paths, lines, success, part2):

    while len(paths) > 0:
        x,y,visited = paths.pop()

        if 0 <= x < len(lines) and 0 <= y < len(lines[0]):
            c = lines[x][y]

            if x == len(lines) - 1 and c == '.':
                success.append(visited.copy())
                print(len(visited))
            elif (x,y) not in visited:
                if c != '#':
                    visited.append((x,y))

                if part2:
                    if c != '#':
                        paths.append((x - 1, y, visited.copy()))
                        paths.append((x + 1, y, visited.copy()))
                        paths.append((x, y - 1, visited.copy()))
                        paths.append((x, y + 1, visited.copy()))

                else:
                    if c == '.':
                        paths.append((x - 1, y, visited.copy()))
                        paths.append((x + 1, y, visited.copy()))
                        paths.append((x, y - 1, visited.copy()))
                        paths.append((x, y + 1, visited.copy()))
                    elif c == '<':
                        paths.append((x, y - 1, visited))
                    elif c == '>':
                        paths.append((x, y + 1, visited))
                    elif c == '^':
                        paths.append((x - 1, y, visited))
                    elif c == 'v':
                        paths.append((x + 1, y, visited))


if __name__ == '__main__':
    assert day23('day23_test.txt', False) == 94
    assert day23('day23_input.txt', False) == 2238

    assert day23('day23_test.txt', True) == 154
    #assert day23('day23_input.txt', True) == 2238


