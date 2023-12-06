
def day3():
    print('Day 3 gears')
    x = 0
    with open('day3_input.txt') as f:
        lines = [line.strip() for line in f.readlines()]
        x = gears(lines)
    return x


def gears(lines):
    part_nums = []
    part2 = {}
    for row, line in enumerate(lines):
        res = False
        cur = ''
        stars = {}
        for column, c in enumerate(line):
            if c.isdigit():
                cur = cur + c
                nw = row != 0 and column != 0 and is_symbol(lines, row - 1,column - 1, stars)
                n = row != 0 and is_symbol(lines,row - 1,column, stars)
                ne = row != 0 and column != len(line) - 1 and is_symbol(lines, row - 1, column + 1, stars)
                w = column != 0 and is_symbol(lines, row, column - 1, stars)
                e = column != len(line) - 1 and is_symbol(lines, row, column + 1, stars)
                sw = row != len(lines) - 1 and column != 0 and is_symbol(lines, row + 1, column - 1, stars)
                s = row != len(lines) - 1 and is_symbol(lines, row + 1, column, stars)
                se = row != len(lines) - 1 and column != len(line) - 1 and is_symbol(lines, row + 1, column + 1, stars)
                res = res or (nw or n or ne or w or e or sw or s or se)
                print(row, column, res, cur)
            elif len(cur) > 0:
                if res:
                    part_nums.append(int(cur))

                for star in stars.keys():
                    existing = part2.get(star)
                    if existing:
                        existing.append(int(cur))
                    else:
                        part2[star] = [int(cur)]

                cur = ''
                res = False
                stars = {}

        if len(cur) > 0:
            print(cur)
            if res:
                part_nums.append(int(cur))

            for star in stars.keys():
                existing = part2.get(star)
                if existing:
                    existing.append(int(cur))
                else:
                    part2[star] = [int(cur)]
    print(part_nums)
    print(part2)
    part2_out = 0
    for v in part2.values():
        if len(v) == 2:
            part2_out += v[0] * v[1]
    return sum(part_nums), part2_out


def is_symbol(lines, x, y, stars: dict):
    c = lines[x][y]
    if c == '*':
        stars[(x,y)] = True
    return not c.isdigit() and not c == '.'


if __name__ == '__main__':
    print(day3())