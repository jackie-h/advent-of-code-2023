from collections import deque


def day16(filename, part2):
    print('Day 16: The Floor Will Be Lava')

    res = 0
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
        res = solve(lines, part2)
        print(res)

    return res


def solve(lines, part2):
    res = 0

    dir = (0,1)
    start = (0,0)
    sc = lines[0][0]
    if sc == '\\':
       dir = (1,0)

    beams = deque()
    beams.append((start,dir))

    visited = set()
    locations_visited = set()

    while len(beams) > 0:
        location, direction = beams.popleft()
        locations_visited.add(location)
        nx = location[0] + direction[0]
        ny = location[1] + direction[1]

        stop = (location,direction) in visited
        stop = stop or ((nx == len(lines) - 1) and (ny == len(lines[0]) - 1))
        stop = stop or nx < 0 or nx >= len(lines)
        stop = stop or ny < 0 or ny >= len(lines[0])

        if not stop:
            print(location)
            visited.add((location,direction))
            m = lines[nx][ny]

            if m == '.':
                beams.append(((nx,ny),direction))
            if m == '\\':
                # 0,1 = 1,0
                # 1,0 = 0,1
                # 0,-1 = -1,0
                # -1,0 = 0,-1
                beams.append(((nx, ny), (direction[1],direction[0])))
            elif m == '/':
                #0,1 = -1,0
                #1,0 = 0,-1
                #0,-1 = 1,0
                #-1,0 = 0,1
                if direction[0] == 0:
                    nd = (-direction[1],0)
                else:
                    nd = (0,-direction[0])
                beams.append(((nx, ny), nd))
            elif m == '|':
                if direction[0] == 0:
                    beams.append(((nx, ny), (-1,0)))
                    beams.append(((nx, ny), (1,0)))
                else:
                    beams.append(((nx, ny), direction))
            elif m == '-':
                if direction[1] == 0:
                    beams.append(((nx, ny), (0,-1)))
                    beams.append(((nx, ny), (0,1)))
                else:
                    beams.append(((nx, ny), direction))

    res = len(locations_visited)
    return res



if __name__ == '__main__':
    #assert day16('day16_test.txt', False) == 46
    assert day16('day16_input.txt', False) == 46


