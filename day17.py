from heapq import heappop, heappush


def day17(filename, min_dist, max_dist):
    print('Day 17: Clumsy Crucible')

    res = 0
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
        res = solve(lines, min_dist, max_dist)
        print(res)

    return res


def solve(lines, min_dist, max_dist):
    q = [(0, (0, 0), (0, 0))]  # cost, location, direction
    visited = set()
    costs = {}

    while q:
        cost, location, prev_direction = heappop(q)
        x, y = location

        # We are at the goal
        if x == len(lines) - 1 and y == len(lines[0]) - 1:
            return cost

        if (location, prev_direction) not in visited:
            visited.add((location, prev_direction))

            directions = next_directions(prev_direction)
            for direction in directions:
                cost_increase = 0
                #print(direction)

                for distance in range(1, max_dist + 1):
                    nx = x + direction[0] * distance
                    ny = y + direction[1] * distance
                    if 0 <= nx < len(lines) and 0 <= ny < len(lines[0]):
                        cost_increase += int(lines[nx][ny])
                        if distance < min_dist:
                            continue
                        nc = cost + cost_increase
                        if costs.get((nx, ny, direction), 1e100) <= nc:
                            continue
                        costs[(nx, ny, direction)] = nc
                        print(nx,ny,direction,nc)
                        heappush(q, (nc, (nx, ny), direction))


def next_directions(direction):
    n = (-1, 0)
    s = (1, 0)
    e = (0, 1)
    w = (0, -1)

    if direction == n:
        return [e,w]
    elif direction == s:
        return [e, w]
    elif direction == e:
        return [s, n]
    elif direction == w:
        return [s, n]
    else:
        return [e,s,n,w]


if __name__ == '__main__':
    assert day17('day17_test.txt', 1, 3) == 102
    assert day17('day17_input.txt', 1, 3) == 1039

    assert day17('day17_test.txt', 4, 10) == 94
    assert day17('day17_input.txt', 4, 10) == 1201
