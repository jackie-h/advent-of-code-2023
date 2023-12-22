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

    coords = []
    for line in lines:
        head,tail = line.split("~")
        x,y,z = head.split(",")
        a,b,c = tail.split(",")
        coords.append(((x,y,z),(a,b,c)))

    sorted(coords, key=itemgetter(2))



    return res



if __name__ == '__main__':
    assert day22('day22_test.txt', False) == 5


