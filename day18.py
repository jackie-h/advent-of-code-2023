
def day18(filename, part2):
    print('Day 18: Lavaduct Lagoon')

    res = 0
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
        res = solve(lines, part2)
        print(res)

    return res


def solve(lines, part2):
    res = 0

    if not part2:
        size = 5
        grid = [['.']*size for i in range(size)]
        cx, cy = 0,0
        grid[cx][cy] = '#'
        for line in lines:
            d,v,c = line.split()
            ix = 0
            iy = 0
            if d == 'R':
                iy = 1
            elif d == 'L':
                iy = -1
            elif d == 'D':
                ix = 1
            elif d == 'U':
                ix = -1

            for i in range(0,int(v)):
                cx = cx + ix
                cy = cy + iy
                if cx < 0:
                    width = len(grid[0])
                    row = ['.']*width
                    grid.insert(0,row)
                    if cx < 0:
                        cx += 1
                elif cx >= len(grid):
                    grid.append(['.']*len(grid[0]))
                elif cy < 0:
                    for i in range(0,len(grid)):
                        grid[i].insert(0,'.')
                    cy += 1
                elif cy >= len(grid[0]):
                    for i in range(0,len(grid)):
                        grid[i].insert(cy,'.')

                grid[cx][cy] = '#'

        for x in range(0,len(grid)):
            print(*grid[x], sep="")
        # print('\n'.join(' '.join(str(x) for x in row) for row in grid))


        #Fill
        for i in range(0,len(grid)):
            dot_count = 0
            seen_hash = False
            for j in range(0,len(grid[0])):
                if grid[i][j] == '#':
                    seen_hash = True
                    res += 1
                    if dot_count > 0:
                        seen_hash = False
                        res += dot_count
                        dot_count = 0
                else:
                    if seen_hash:
                        dot_count += 1

    else:
        print('')

    return res


if __name__ == '__main__':
    assert day18('day18_test.txt', False) == 62
    assert day18('day18_input.txt', False) == 62



