import itertools


def day24(filename, x_min, x_max):
    print('Day 24: Never Tell Me The Odds')

    res = 0
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
        res = solve(lines, x_min, x_max)
        print(res)

    return res


def solve(lines, x_min, x_max):
    res = 0

    coords = []
    for line in lines:
        head, tail = line.split(" @ ")
        x, y, z = head.split(", ")
        a, b, c = tail.split(", ")
        coords.append(((int(x), int(y), int(z)), (int(a), int(b), int(c))))

    for a,b in itertools.combinations(coords, 2):
        p1, v1 = a
        p2, v2 = b

        apx, apy, apz = p1
        avx, avy, avz = v1
        bpx, bpy, bpz = p2
        bvx, bvy, bvz = v2
        ma = (avy / avx)
        mb = (bvy / bvx)
        if ma == mb:
            continue
        ca = apy - (ma * apx)
        cb = bpy - (mb * bpx)
        x_pos = (cb - ca) / (ma - mb)
        y_pos = ma * x_pos + ca
        if (x_pos < apx and avx > 0) or (x_pos > apx and avx < 0) or (x_pos < bpx and bvx > 0) or (x_pos > bpx and bvx < 0):
            continue
        if x_min <= x_pos <= x_max and x_min <= y_pos <= x_max:
            res += 1

    return res


if __name__ == '__main__':
    x_min, x_max = 7, 27
    assert day24('day24_test.txt', x_min, x_max) == 2

    x_min, x_max = 200000000000000, 400000000000000
    assert day24('day24_input.txt', x_min, x_max) == 16665
