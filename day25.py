import collections
from itertools import combinations

def day25(filename, part2):
    print('Day 25: Snowverload')

    res = 0
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
        res = solve(lines, part2)
        print(res)

    return res


def solve(lines, part2):
    res = 0
    connections = {}
    pairs = []

    for line in lines:
        head,tail = line.split(": ")
        t = tail.split(" ")
        c = connections.get(head)
        if c is None:
            connections[head] = t
        else:
            c.extend(t)

        for v in t:
            pairs.append((head, v))
            c = connections.get(v)
            if c is None:
                connections[v] = [head]
            else:
                c.append(head)

    lc = 0
    for c in combinations(pairs, 3):
        lc += 1
        res = count_cycles(connections, set(c), 2)
        print(lc, c, res)
        if res > 1:
            break

    return res


def count_cycles(connections:dict, disconnected, target_cycles):
    keys:set = set(connections.keys())
    cycles = 0
    groups = []

    while len(keys) > 0:
        cycles += 1
        if cycles > target_cycles:
            break
        q = collections.deque()
        q.append(next(iter(keys)))

        visited = set()

        while q:
            k = q.popleft()
            if k not in visited:
                vals = connections.get(k)
                visited.add(k)
                keys.remove(k)
                for v in vals:
                    if (k,v) not in disconnected and (v,k) not in disconnected:
                            q.append(v)
        groups.append(visited)

    res = 1
    if cycles == target_cycles:
        for g in groups:
            res = res*len(g)

    return res


if __name__ == '__main__':
    assert day25('day25_test.txt', False) == 54
    assert day25('day25_input.txt', False) == 0


