import re


def day11(filename, expansion):
    print('Day 11: Cosmic Expansion')

    res = 0
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
        res = solve(lines, expansion)
        print(res)

    return res


def solve(lines, expansion):

    points = []
    rows2expand = []
    for i,line in enumerate(lines):
        occ = [m.start() for m in re.finditer('#', line)]
        if len(occ) == 0:
            rows2expand.append(i)
        else:
            for o in occ:
                points.append((i,o))

    cols2expand = []
    for c in range(0,len(lines[0])):
        expand = True
        for r in range(0,len(lines)):
            x = lines[r][c]
            if x != '.':
                expand = False
                break
        if expand:
            cols2expand.append(c)

    distance = 0

    while len(points) > 0:
        a = points.pop()
        for b in points:
            if a != b:
                sx = a[0] if a[0] < b[0] else b[0]
                ex = b[0] if b[0] > a[0] else a[0]
                sy = a[1] if a[1] < b[1] else b[1]
                ey = b[1] if b[1] > a[1] else a[1]
                xd = ex - sx
                yd = ey - sy
                for r in rows2expand:
                    if sx < r < ex:
                        xd += expansion - 1
                    elif r > ex:
                        break
                for c in cols2expand:
                    if sy <= c <= ey:
                        yd += expansion - 1
                    elif c > ey:
                        break
                d = xd + yd
                #print('d=', d, (a,b))
                distance += d

    return distance


if __name__ == '__main__':
    assert day11('day11_test.txt',2) == 374
    assert day11('day11_input.txt',2) == 9536038
    assert day11('day11_test.txt', 10) == 1030
    assert day11('day11_test.txt', 100) == 8410
    assert day11('day11_input.txt', 1000000) == 447744640566

