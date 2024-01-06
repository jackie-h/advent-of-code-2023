import collections
import operator
from itertools import combinations
from random import randrange


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
    connections = collections.defaultdict(set)
    pairs = []

    for line in lines:
        head, tail = line.split(": ")
        t = tail.split(" ")
        for v in t:
            pairs.append((head, v))
            connections[v].add(head)
            connections[head].add(v)

    # pairs_combos = find_most_popular_connections(connections)

    # lc = 0
    # for c in combinations(pairs, 3):
    #     lc += 1
    #     res = count_cycles(connections, set(c), 2)
    #     print(lc, c, res)
    #     if res > 1:
    #         break

    keys = set(connections)
    count = lambda v: len(connections[v] - keys)

    while sum(map(count, keys)) != 3:
        keys.remove(max(keys, key=count))

    res = len(keys) * len(set(connections) - keys)

    return res


def find_most_popular_connections(connections):
    kl = list(connections.keys())
    crossings = {}
    for i in range(10):
        r1 = randrange(len(kl))
        r2 = randrange(len(kl))
        print(kl[r1], kl[r2])
        ps = find_path(connections, kl[r1], kl[r2])
        for p in ps:
            ct = crossings.get(p)
            if ct is None:
                crossings[p] = 1
            else:
                crossings[p] = 1 + ct
    sorted_crossings = sorted(crossings.items(), key=operator.itemgetter(1), reverse=True)
    pairs_combos = sorted_crossings[0:20]
    return pairs_combos


def find_path(connections: dict, key1, key2):
    q = collections.deque()
    for v in connections.get(key1):
        q.append((key1, v, set()))

    success = []

    while q:
        prev, k, visited = q.popleft()
        if k == key2:
            success = visited
            break

        if (prev, k) not in visited:
            visited.add((prev, k))
            vals = connections.get(k)
            for v in vals:
                q.append((k, v, visited.copy()))
    return success


def count_cycles(connections: dict, disconnected, target_cycles):
    keys: set = set(connections.keys())
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
                    if (k, v) not in disconnected and (v, k) not in disconnected:
                        q.append(v)
        groups.append(visited)

    res = 1
    if cycles == target_cycles:
        for g in groups:
            res = res * len(g)

    return res


if __name__ == '__main__':
    # ('jqt', 'nvd'), ('cmg', 'bvb'), ('pzl', 'hfx')
    assert day25('day25_test.txt', False) == 54
    assert day25('day25_input.txt', False) == 583632
