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

    for p in itertools.combinations(coords, 2):
        i1, i2 = p
        p1, v1 = i1
        p2, v2 = i2
        d1 = diff_coords(p1, p2)
        np1 = move(p1, v1, 1)
        np2 = move(p2, v2, 1)
        d2 = diff_coords(np1, np2)
        print(p1, p2, d1, np1, np2, d2)
        if d2 < d1:
            t1 = max_t_inside(p1, v1, x_min, x_max)
            t2 = max_t_inside(p2, v2, x_min, x_max)
            t = min(t1,t2)
            mp1 = move(p1, v1, t)
            mp2 = move(p2, v2, t)
            d3 = diff_coords(mp1, mp2)
            if d3 > d2:
                res += 1
                print('yes=', p1, p2)

    # x + t*v = x1 + t*v2

    return res

def max_t_inside(p1,v1,min_x,max_x):
    x,y,z = p1
    vx,vy,vz = v1
    t = 0
    if vx < 0:
        tx = (x - min_x) / abs(vx)
    else:
        tx = (max_x - x) / vx

    if vy < 0:
        ty = (y - min_x) / abs(vy)
    else:
        ty = (max_x - y) / vy
    t = min(ty,tx)
    return t


def move(p1, v1, t):
    return p1[0] + t * v1[0], p1[1] + t * v1[1], p1[2] + t * v1[2]


def diff_coords(p1, p2):
    diff = (p1[0] - p2[0], p1[1] - p2[1], p1[2] - p2[2])
    #Just x and y for part 1
    total = abs(diff[0]) + abs(diff[1])
    return total


if __name__ == '__main__':
    x_min, x_max = 7, 27
    assert day24('day24_test.txt', x_min, x_max) == 2
