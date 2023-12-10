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


    print('S=', r,c)


    grid = [ [-2]*width for _ in range(height) ]

    starts = [(r, c,'n'),(r, c,'s'),(r, c,'w'),(r, c,'e')]
    grid[r][c] = 0
    print('starts',starts)
    res = follow_path(starts, -1, grid, height, lines, width)
    print('grid', grid)
    print(res)

    inside = 0
    if part2:
        edge_start = find_edge_start(grid, width, height)
        while edge_start is not None:
            print(edge_start)
            x,y = edge_start
            if x == 0:
                fill(('s', x, y), grid, height, width, lines)
            else:
                fill(('n', x, y), grid, height, width, lines)
            if y == 0:
                fill(('e', x, y), grid, height, width, lines)
            else:
                fill(('w', x, y), grid, height, width, lines)
                #fill(('e', x, y), grid, height, width)
            edge_start = find_edge_start(grid, width, height)


        for x in range(0,height):
            for y in range(0,width):
                v = grid[x][y]
                if v != 'o' and v < 0:
                    inside += 1

        print('grid', grid)
        for row in grid:
            print(*row, sep="\t")
        #print('\n'.join(' '.join(str(x) for x in row) for row in grid))

    if part2:
        return inside
    else:
        return res


def fill(location, grid, height, width, lines):
    d, r, c = location

    if d == 'n' and in_bounds(r-1,c,height,width):
        v = grid[r-1][c]
        if v != 'o' and v < 0:
            grid[r - 1][c] = 'o'
            fill(('n', r - 1, c), grid, height, width, lines)
            fill(('w', r - 1, c), grid, height, width, lines)
            fill(('e', r - 1, c), grid, height, width, lines)
        else:
            v = lines[r-1][c]
            if c < width - 1 and v in ['|', 'J','7']:
                a = grid[r-1][c+1]
                av = lines[r-1][c+1]
                if a != 'o' and a < 0:
                    grid[r - 1][c+1] = 'o'
                    fill(('n', r - 1, c), grid, height, width, lines)
                    fill(('n', r - 1, c+1), grid, height, width, lines)
                elif av in ['|','F','L']:
                    fill(('n', r - 1, c), grid, height, width, lines)
    elif d == 's' and in_bounds(r+1,c,height,width):
        v = grid[r+1][c]
        if v != 'o' and v < 0:
            grid[r+1][c] = 'o'
            fill(('s', r + 1, c), grid, height, width, lines)
            fill(('w', r + 1, c), grid, height, width, lines)
            fill(('e', r + 1, c), grid, height, width, lines)
        else:
            v = lines[r+1][c]
            if c < width - 1 and v in ['|', 'J','7']:
                a = grid[r+1][c+1]
                av = lines[r+1][c+1]
                if a != 'o' and a < 0:
                    grid[r + 1][c + 1] = 'o'
                    fill(('s', r + 1, c), grid, height, width, lines)
                    fill(('s', r + 1, c + 1), grid, height, width, lines)
                elif av in ['|','F','L']:
                    fill(('s', r + 1, c), grid, height, width, lines)
    elif d == 'w' and in_bounds(r,c-1,height,width):
        nc = c -1
        v = grid[r][nc]
        if v != 'o' and v < 0:
            grid[r][nc] = 'o'
            fill(('s', r, nc), grid, height, width, lines)
            fill(('w', r, nc), grid, height, width, lines)
            fill(('n', r, nc), grid, height, width, lines)
        else:
            v = lines[r][nc]
            if r < height - 1 and v in ['-', 'J','L']:
                a = grid[r+1][nc]
                av = lines[r+1][nc]
                if a != 'o' and a < 0:
                    grid[r+1][nc] = 'o'
                    fill(('w', r, nc), grid, height, width, lines)
                    fill(('w', r+1, nc), grid, height, width, lines)
                elif av in ['-','F','7']:
                    fill(('w', r, nc), grid, height, width, lines)
    elif d == 'e' and in_bounds(r,c+1,height,width):
        nc = c +1
        v = grid[r][nc]
        if v != 'o' and v < 0:
            grid[r][nc] = 'o'
            fill(('s', r, nc), grid, height, width, lines)
            fill(('e', r, nc), grid, height, width, lines)
            fill(('n', r, nc), grid, height, width, lines)
        else:
            v = lines[r][nc]
            if r < height - 1 and v in ['-', 'J','L']:
                a = grid[r+1][nc]
                av = lines[r+1][nc]
                if a != 'o' and a < 0:
                    grid[r+1][nc] = 'o'
                    fill(('e', r, nc), grid, height, width, lines)
                    fill(('e', r+1, nc), grid, height, width, lines)
                elif av in ['-','F','7']:
                    fill(('e', r, nc), grid, height, width, lines)

def find_edge_start(grid, width, height):
    for x in range(0,height):
        for y in [0, width - 1]:
            v = grid[x][y]
            if v != 'o' and v < 0:
                grid[x][y] = 'o'
                return (x, y)

    for y in range(0, width):
        for x in [0, height - 1]:
            v = grid[x][y]
            if v != 'o' and v < 0:
                grid[x][y] = 'o'
                return (x, y)

    return None

def follow_path(paths, count, grid, height, lines, width):

    while len(paths) > 0:
        new_paths = []
        count += 1
        for location in paths:

            r, c, d = location
            #print('current', location, lines[r][c])
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
    #assert day10('day10_test1.txt') == 4
    #assert day10('day10_input.txt') == 6613
    #assert day10('day10_test2.txt', True) == 4
    #assert day10('day10_test3.txt', True) == 4
    assert day10('day10_test4.txt', True) == 8
    assert day10('day10_test5.txt', True) == 10

    assert day10('day10_input.txt', True) == 10