def day10(filename):
    print('Day 10: Pipe Maze')

    res = 0
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
        res = solve(lines)
        print(res)

    return res


def solve(lines):
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


    print('S=', r,c)


    grid = [ [-2]*width for _ in range(height) ]

    starts = [(r, c,'n'),(r, c,'s'),(r, c,'w'),(r, c,'e')]
    grid[r][c] = 0
    print('starts',starts)
    res = follow_path(starts, -1, grid, height, lines, width)
    print('grid', grid)
    print(res)
    return res


def follow_path(paths, count, grid, height, lines, width):

    while len(paths) > 0:
        new_paths = []
        count += 1
        for location in paths:

            r, c, d = location
            print('current', location, lines[r][c])
            location = None

            # North
            if d == 'n' and is_valid(r - 1, c, height, width, grid):
                ns = lines[r - 1][c]
                if ns == '.':
                    grid[r - 1][c] = -1
                elif ns == '|':
                    location = (r - 1, c, 'n')
                    grid[r - 1][c] = count
                elif ns == '7':
                    location = (r - 1, c, 'w')
                    grid[r - 1][c] = count
                elif ns == 'F':
                    location = (r - 1, c, 'e')
                    grid[r - 1][c] = count
            # South
            elif d == 's' and is_valid(r + 1, c, height, width, grid):
                ss = lines[r + 1][c]
                if ss == '.':
                    grid[r + 1][c] = -1
                elif ss == '|':
                    location = (r + 1, c, 's')
                    grid[r + 1][c] = count
                elif ss == 'J':
                    location = (r + 1, c, 'w')
                    grid[r + 1][c] = count
                elif ss == 'L':
                    location = (r + 1, c, 'e')
                    grid[r + 1][c] = count
            # West
            elif d == 'w' and is_valid(r, c - 1, height, width, grid):
                ws = lines[r][c - 1]
                if ws == '.':
                    grid[r][c - 1] = -1
                elif ws == '-':
                    location = (r, c - 1, 'w')
                    grid[r][c - 1] = count
                elif ws == 'L':
                    location = (r, c - 1, 'n')
                    grid[r][c - 1] = count
                elif ws == 'F':
                    location = (r, c - 1, 's')
                    grid[r][c - 1] = count
            # East
            elif d == 'e' and is_valid(r, c + 1, height, width, grid):
                es = lines[r][c + 1]
                if es == '.':
                    grid[r][c + 1] = -1
                elif es == '-':
                    location = (r, c + 1, 'e')
                    grid[r][c + 1] = count
                elif es == 'J':
                    location = (r, c + 1, 'n')
                    grid[r][c + 1] = count
                elif es == '7':
                    location = (r, c + 1, 's')
                    grid[r][c + 1] = count
            if location is not None:
                new_paths.append(location)
        paths = new_paths
    return count


def is_valid(r, c, height, width, grid):
    return in_bounds(r, c, height, width) and grid[r][c] == -2


def in_bounds(r, c, height, width):
    return 0 <= r < height and 0 <= c < width


if __name__ == '__main__':
    assert day10('day10_test1.txt') == 4
    assert day10('day10_input.txt') == 6613