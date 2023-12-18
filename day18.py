
def day18(filename, part2):
    print('Day 18: Lavaduct Lagoon')

    res = 0
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
        res = solve(lines, part2)
        print(res)

    return res


def solve(lines, part2):
    res = 0

    if not part2:
        cx, cy = 0,0
        border_len = 1
        coords = [(cx, cy)]
        for line in lines:
            d,sv,c = line.split()
            v = int(sv)
            ix = 0
            iy = 0
            if d == 'R':
                iy = 1
            elif d == 'L':
                iy = -1
            elif d == 'D':
                ix = 1
            elif d == 'U':
                ix = -1

            cx = cx + ix * v
            cy = cy + iy * v
            border_len += v
            coords.append((cx,cy))

        # area
        area = 0
        for i in range(1, len(coords)):
            x1, y1 = coords[i - 1]
            x2, y2 = coords[i]
            area += (y1 + y2) * (x1 - x2)

        area = (abs(area) + border_len + 1) / 2
        res = area

    else:
        print('')

    return res


if __name__ == '__main__':
    assert day18('day18_test.txt', False) == 62
    assert day18('day18_test2.txt', False) == 33
    assert day18('day18_input.txt', False) == 70026



