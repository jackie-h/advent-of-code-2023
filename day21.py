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
            check_and_move(x - 1, y, lines, new_locations, part2)
            check_and_move(x + 1, y, lines, new_locations, part2)
            check_and_move(x, y - 1, lines, new_locations, part2)
            check_and_move(x, y + 1, lines, new_locations, part2)
        locations = new_locations

    res = len(locations)
    return res


def check_and_move(cx, cy, lines, new_locations, part2):
    lx = cx
    ly = cy
    if cx < 0 or cx >= len(lines):
        if part2:
            lx = cx%len(lines)
        else:
            return
    if cy < 0 or cy >= len(lines[0]):
        if part2:
            ly = cy%len(lines[0])
        else:
            return

    if lines[lx][ly] != '#':
        new_locations.add((cx, cy))


if __name__ == '__main__':
    assert day21('day21_test.txt', False, 6) == 16
    assert day21('day21_input.txt', False, 64) == 3841

    assert day21('day21_test.txt', True, 6) == 16
    assert day21('day21_test.txt', True, 10) == 50
    assert day21('day21_test.txt', True, 50) == 1594
    assert day21('day21_test.txt', True, 100) == 6536
    assert day21('day21_test.txt', True, 500) == 167004
    assert day21('day21_test.txt', True, 1000) == 668697
    assert day21('day21_test.txt', True, 5000) == 16733044

