from collections import defaultdict

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
    new_coords = settle(coords)

    res = can_remove(new_coords)

    return res

def settle(coords):
    prev_lk = 1
    new_coords = defaultdict(set)
    for k,v in coords.items():
        for block in v:
            new_bz = block[0][2]
            clear = True
            while clear and new_bz != 1:
                tk = min(prev_lk, new_bz - 1)
                new_bz = tk
                for c in new_coords[tk]:
                    overlap = x_y_overlap(block, c)
                    print('overlap',block,c,overlap)
                    clear = not overlap
                    if not clear:
                        new_bz = max(new_bz,c[1][2] + 1)

            diff = k - new_bz
            new_c = ((block[0][0], block[0][1],new_bz), (block[1][0], block[1][1], block[1][2] - diff))
            print(block,new_c,new_bz,diff)
            new_coords[new_bz].add(new_c)
        prev_lk = k


    return new_coords


def can_remove(coords):
    count = 0
    bf,bv = 0,[]

    support_counts = {}

    keys = list(coords.keys())
    for k in reversed(keys):
        below_k = k - 1
        if k > 0:
            for block in coords[k]:
                support_count = 0
                for c in coords[below_k]:
                    overlap = x_y_overlap(block, c)
                    print('supporting', block, c, overlap)
                    if overlap:
                        support_count += 1
                    if support_count >= 2:
                        break
                print('supporting count',block, support_count, support_count == 0 or support_count >= 2)
                support_counts[block] = support_count

    keys = list(coords.keys())
    for k in keys:
        above_k = k + 1
        for block in coords[k]:
            is_supporting = False
            for c in coords[above_k]:
                overlap = x_y_overlap(block, c)
                print('supporting', block, c, overlap)
                if overlap:
                    supports = support_counts[c]
                    is_supporting = supports == 1
                if is_supporting:
                    break
            print('can remove',block, not is_supporting)
            if not is_supporting:
                count += 1

    return count


def x_y_overlap(block1, block2):
    b1_x1 = block1[0][0]
    b1_x2 = block1[1][0]
    b2_x1 = block2[0][0]
    b2_x2 = block2[1][0]
    x_overlap = b1_x1 in range(b2_x1, b2_x2+1) or b1_x2 in range(b2_x1, b2_x2+1) \
            or b2_x1 in range(b1_x1, b1_x2+1) or b2_x2 in range(b1_x1, b1_x2+1)
    if not x_overlap:
        return False
    b1_y1 = block1[0][1]
    b1_y2 = block1[1][1]
    b2_y1 = block2[0][1]
    b2_y2 = block2[1][1]
    y_overlap = b1_y1 in range(b2_y1,b2_y2+1) or b1_y2 in range(b2_y1,b2_y2+1) \
            or b2_y1 in range(b1_y1,b1_y2+1) or b2_y2 in range(b1_y1,b1_y2+1)
    if not y_overlap:
        return False
    return x_overlap and y_overlap


if __name__ == '__main__':
    assert day22('day22_test.txt', False) == 5
    assert day22('day22_test2.txt', False) == 1
    #assert day22('day22_input.txt', False) == 5
