def day21(filename, part2, total_steps):
    print('Day 21: Step Counter')

    res = 0
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
        res = solve(lines, part2, total_steps)
        print(res)

    return res


def solve(lines, part2, total_steps):
    res = 0

    start = None
    for i,line in enumerate(lines):
        s = line.find('S')
        if s > -1:
            start = (i,s)

    steps = 0

    locations = set()
    locations.add(start)
    for i in range(0,total_steps):
        new_locations = set()
        for x,y in locations:
            if x > 0:
                check_and_move(x - 1, y, lines, new_locations)
            if x < len(lines) - 1:
                check_and_move(x + 1, y, lines, new_locations)
            if y > 0:
                check_and_move(x, y-1, lines, new_locations)
            if y < len(lines[0]) - 1:
                check_and_move(x, y+1, lines, new_locations)
        locations = new_locations

    res = len(locations)
    return res


def check_and_move(cx, cy, lines, new_locations):
    if lines[cx][cy] != '#':
        new_locations.add((cx, cy))


if __name__ == '__main__':
    assert day21('day21_test.txt', False, 6) == 16
    assert day21('day21_input.txt', False, 64) == 3841

    assert day21('day21_test.txt', True, 6) == 16
    assert day21('day21_test.txt', True, 10) == 50

