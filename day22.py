from collections import defaultdict
from operator import itemgetter


def day22(filename, part2):
    print('Day 22: Sand Slabs')

    res = 0
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
        res = solve(lines, part2)
        print(res)

    return res


def solve(lines, part2):
    res = 0

    coords = defaultdict(set)
    for line in lines:
        head, tail = line.split("~")
        x, y, z = head.split(",")
        a, b, c = tail.split(",")
        coords[int(z)].add(((int(x), int(y), int(z)), (int(a), int(b), int(c))))

    sorted(coords, reverse=True)
    settle(coords)

    return res

def settle(coords):
    bf,bv = 0,[]
    new_coords = defaultdict(set)
    for k,v in coords.items():
        if k > 1:
            if k - 1 != bf:
                nk = bf + 1
                for block in v:
                    diff = k - nk
                    new_coords[nk].add(((block[0][0],block[0][1],nk),(block[1][0],block[1][1],block[1][2] - diff)))

            else:
                new_coords[k] = v
        else:
            new_coords[k] = v
        bf = k
        bv = v

    return new_coords

if __name__ == '__main__':
    assert day22('day22_test.txt', False) == 5
