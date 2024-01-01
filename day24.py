from operator import itemgetter


def day24(filename, part2):
    print('Day 24: Never Tell Me The Odds')

    res = 0
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
        res = solve(lines, part2)
        print(res)

    return res


def solve(lines, part2):
    res = 0

    coords = []
    for line in lines:
        head,tail = line.split(" @ ")
        x,y,z = head.split(", ")
        a,b,c = tail.split(", ")
        coords.append(((int(x),int(y),int(z)),(int(a),int(b),int(c))))

    sorted(coords, key=itemgetter(2))

 #x + t*v = x1 + t*v2

    return res



if __name__ == '__main__':
    assert day24('day24_test.txt', False) == 5


