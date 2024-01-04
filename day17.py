import collections


def day17(filename, part2):
    print('Day 17: Clumsy Crucible')

    res = 0
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
        res = solve(lines, part2)
        print(res)

    return res


def solve(lines, part2):

    paths = collections.deque()
    success = []

    start = (0,0)

    paths.append((start, (0, 1), 1, set(), 0))
    paths.append((start, (1, 0), 1, set(), 0))

    best_total = len(lines) * 9 * 2

    while len(paths) > 0:
        location, direction, direction_count, visited, total = paths.pop()

        nx = location[0] + direction[0]
        ny = location[1] + direction[1]

        if (location, direction) not in visited \
                and 0 <= nx < len(lines) and 0 <= ny < len(lines[0]):

            print(location)
            visited.add((location, direction))

            if nx == len(lines) - 1 and ny == len(lines[0]) - 1:
                success.append(visited.copy())
                print('Success')
                best_total = min(total, best_total)
            else:
                total += int(lines[location[0]][location[1]])
                if total < best_total:
                    direction_count,directions = next_directions(direction_count, direction)
                    for dir in directions:
                        paths.append(((nx, ny), dir, direction_count, visited.copy(), total))
                else:
                    print('stop')

    return best_total


def next_directions(direction_count, direction):
    n = (-1,0)
    s = (1,0)
    e = (0,1)
    w = (0,-1)
    directions = []

    if direction_count >= 3:
        direction_count = 1
    else:
        directions.append(direction)
        direction_count = direction_count + 1

    if direction == n or direction == s:
        directions.append(e)
        directions.append(w)
    elif direction == e or direction == w:
        directions.append(n)
        directions.append(s)

    return direction_count,directions


if __name__ == '__main__':
    assert day17('day17_test.txt', False) == 102
