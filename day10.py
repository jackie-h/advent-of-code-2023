import sys


def day10(filename, part2):
    print('Day 10: Pipe Maze')

    res = 0
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
        res = solve(lines, part2)
        print(res)

    return res


def solve(lines, part2):
    sys.setrecursionlimit(10000)

    res = 0
    width = len(lines[0])
    height = len(lines)

    r = 0
    c = -1
    s = ''
    while s != 'S':
        c += 1
        if c == width:
            c = 0
            r += 1
        s = lines[r][c]

    print('S=', r, c)
    visited = set()

    starts = [(r, c, 'n'), (r, c, 's'), (r, c, 'w'), (r, c, 'e')]
    print('starts', starts)
    res = follow_path(starts, -1, height, lines, width, visited)
    print('visited', visited)
    print(res)

    inside = 0
    if part2:

        for i, line in enumerate(lines):
            lines[i] = list(line)

        edge_starts = find_edge_start(lines, width, height, visited)
        for edge_start in edge_starts:
            print(edge_start)
            x, y = edge_start
            if x == 0:
                fill(('s', x, y), height, width, lines, visited)
            else:
                fill(('n', x, y), height, width, lines, visited)
            if y == 0:
                fill(('e', x, y), height, width, lines, visited)
            else:
                fill(('w', x, y), height, width, lines, visited)
                # fill(('e', x, y), grid, height, width)

        for x in range(0, height):
            for y in range(0, width):
                v = lines[x][y]
                if v != 'o' and (x, y) not in visited:
                    inside += 1
                    lines[x][y] = '*'

        for row in lines:
            print(*row, sep=" ")
        # print('\n'.join(' '.join(str(x) for x in row) for row in grid))

    if part2:
        return inside
    else:
        return res


def fill(location, height, width, lines, visited):
    d, r, c = location

    if d == 'n' and in_bounds(r - 1, c, height, width):
        v = lines[r - 1][c]
        if v != 'o' and (r - 1, c) not in visited:
            lines[r - 1][c] = 'o'
            fill(('n', r - 1, c), height, width, lines, visited)
            fill(('w', r - 1, c), height, width, lines, visited)
            fill(('e', r - 1, c), height, width, lines, visited)
        else:
            v = lines[r - 1][c]
            if c < width - 1 and v in ['|', 'J', '7']:
                a = lines[r - 1][c + 1]
                if a != 'o' and (r - 1, c + 1) not in visited:
                    lines[r - 1][c + 1] = 'o'
                    fill(('n', r - 1, c), height, width, lines, visited)
                    fill(('n', r - 1, c + 1), height, width, lines, visited)
                elif a in ['|', 'F', 'L']:
                    fill(('n', r - 1, c), height, width, lines, visited)
    elif d == 's' and in_bounds(r + 1, c, height, width):
        v = lines[r + 1][c]
        if v != 'o' and (r + 1, c) not in visited:
            lines[r + 1][c] = 'o'
            fill(('s', r + 1, c), height, width, lines, visited)
            fill(('w', r + 1, c), height, width, lines, visited)
            fill(('e', r + 1, c), height, width, lines, visited)
        else:
            v = lines[r + 1][c]
            if c < width - 1 and v in ['|', 'J', '7']:
                a = lines[r + 1][c + 1]
                if a != 'o' and (r + 1, c + 1) not in visited:
                    lines[r + 1][c + 1] = 'o'
                    fill(('s', r + 1, c), height, width, lines, visited)
                    fill(('s', r + 1, c + 1), height, width, lines, visited)
                elif a in ['|', 'F', 'L']:
                    fill(('s', r + 1, c), height, width, lines, visited)
    elif d == 'w' and in_bounds(r, c - 1, height, width):
        nc = c - 1
        v = lines[r][nc]
        if v != 'o' and (r, nc) not in visited:
            lines[r][nc] = 'o'
            fill(('s', r, nc), height, width, lines, visited)
            fill(('w', r, nc), height, width, lines, visited)
            fill(('n', r, nc), height, width, lines, visited)
        else:
            v = lines[r][nc]
            if r < height - 1 and v in ['-', 'J', 'L']:
                a = lines[r + 1][nc]
                if a != 'o' and (r + 1, nc) not in visited:
                    lines[r + 1][nc] = 'o'
                    fill(('w', r, nc), height, width, lines, visited)
                    fill(('w', r + 1, nc), height, width, lines, visited)
                elif a in ['-', 'F', '7']:
                    fill(('w', r, nc), height, width, lines, visited)
    elif d == 'e' and in_bounds(r, c + 1, height, width):
        nc = c + 1
        v = lines[r][nc]
        if v != 'o' and (r, nc) not in visited:
            lines[r][nc] = 'o'
            fill(('s', r, nc), height, width, lines, visited)
            fill(('e', r, nc), height, width, lines, visited)
            fill(('n', r, nc), height, width, lines, visited)
        else:
            v = lines[r][nc]
            if r < height - 1 and v in ['-', 'J', 'L']:
                a = lines[r + 1][nc]
                if a != 'o' and (r + 1, nc) not in visited:
                    lines[r + 1][nc] = 'o'
                    fill(('e', r, nc), height, width, lines, visited)
                    fill(('e', r + 1, nc), height, width, lines, visited)
                elif a in ['-', 'F', '7']:
                    fill(('e', r, nc), height, width, lines, visited)


def find_edge_start(lines, width, height, visited):
    starts = []
    for x in range(0, height):
        for y in [0, width - 1]:
            v = lines[x][y]
            if v != 'o' and (x, y) not in visited:
                lines[x][y] = 'o'
                starts.append((x, y))
            elif v in ['-','L', 'J'] and x < height - 1 \
                    and lines[x+1][y] in ['-','F','7']:
                starts.append((x, y))

    for y in range(0, width):
        for x in [0, height - 1]:
            v = lines[x][y]
            if v != 'o' and (x, y) not in visited:
                lines[x][y] = 'o'
                starts.append((x, y))
            elif v in ['|', 'J', '7'] and y < width - 1 \
                    and lines[x][y+1] in ['|', 'F', 'L']:
                starts.append((x, y))

    return starts


def follow_path(paths, count, height, lines, width, visited):
    while len(paths) > 0:
        new_paths = []
        count += 1
        for location in paths:

            r, c, d = location
            # print('current', location, lines[r][c])
            location = None
            visited.add((r, c))

            # North
            if d == 'n' and is_valid(r - 1, c, height, width, visited):
                ns = lines[r - 1][c]
                if ns == '|':
                    location = (r - 1, c, 'n')
                elif ns == '7':
                    location = (r - 1, c, 'w')
                elif ns == 'F':
                    location = (r - 1, c, 'e')
            # South
            elif d == 's' and is_valid(r + 1, c, height, width, visited):
                ss = lines[r + 1][c]
                if ss == '|':
                    location = (r + 1, c, 's')
                elif ss == 'J':
                    location = (r + 1, c, 'w')
                elif ss == 'L':
                    location = (r + 1, c, 'e')
            # West
            elif d == 'w' and is_valid(r, c - 1, height, width, visited):
                ws = lines[r][c - 1]
                if ws == '-':
                    location = (r, c - 1, 'w')
                elif ws == 'L':
                    location = (r, c - 1, 'n')
                elif ws == 'F':
                    location = (r, c - 1, 's')
            # East
            elif d == 'e' and is_valid(r, c + 1, height, width, visited):
                es = lines[r][c + 1]
                if es == '-':
                    location = (r, c + 1, 'e')
                elif es == 'J':
                    location = (r, c + 1, 'n')
                elif es == '7':
                    location = (r, c + 1, 's')
            if location is not None:
                new_paths.append(location)
        paths = new_paths
    return count


def is_valid(r, c, height, width, visited: set):
    return in_bounds(r, c, height, width) and (r, c) not in visited  # and grid[r][c] == -2


def in_bounds(r, c, height, width):
    return 0 <= r < height and 0 <= c < width


if __name__ == '__main__':
    # assert day10('day10_test1.txt', False) == 4
    # assert day10('day10_input.txt', False) == 6613
    assert day10('day10_test2.txt', True) == 4
    assert day10('day10_test3.txt', True) == 4
    assert day10('day10_test4.txt', True) == 8
    assert day10('day10_test5.txt', True) == 10

    # West passage
    assert day10('day10_test6.txt', True) == 4

    # East passage
    assert day10('day10_test7.txt', True) == 4
    assert day10('day10_test8.txt', True) == 4

    assert day10('day10_input.txt', True) == 517
