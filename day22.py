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

    new_coords_by_bz, new_coords_by_tz = settle(coords)

    res = can_remove(new_coords_by_bz, new_coords_by_tz, part2)

    return res


def settle(coords):
    prev_lk = 1
    new_coords_by_tz = defaultdict(set)
    new_coords_by_bz = defaultdict(set)
    keys = sorted(coords.keys())
    for k in keys:
        for block in coords.get(k):
            new_bz = block[0][2]
            clear = True
            while clear and new_bz != 1:
                tk = new_bz - 1
                new_bz = tk
                for c in new_coords_by_tz[tk]:
                    overlap = x_y_overlap(block, c)
                    print('overlap', block, c, overlap)
                    if overlap:
                        new_bz = max(new_bz, c[1][2] + 1)
                    clear = clear and not overlap

            new_c = ((block[0][0], block[0][1],new_bz), (block[1][0], block[1][1], new_bz + (block[1][2] - block[0][2])))
            print(block,new_c,new_bz)
            new_coords_by_tz[new_c[1][2]].add(new_c)
            new_coords_by_bz[new_c[0][2]].add(new_c)
        prev_lk = k

    return new_coords_by_bz, new_coords_by_tz


def can_remove(coords_by_bz, coords_by_tz, part2):
    count = 0

    support_counts = {}
    supporting = defaultdict(set)
    supported_by = defaultdict(set)

    keys = sorted(list(coords_by_tz.keys()))
    for k in reversed(keys):
        if k > 1:
            for block in coords_by_tz[k]:
                below_k = block[0][2] - 1
                support_count = 0
                for c in coords_by_tz[below_k]:
                    overlap = x_y_overlap(block, c)
                    print('supporting', block, c, overlap)
                    if overlap:
                        support_count += 1
                        supporting[c].add(block)
                        supported_by[block].add(c)
                    if support_count >= 2:
                        break
                print('supporting count', block, support_count, support_count == 0 or support_count >= 2)
                support_counts[block] = support_count

    keys = sorted(list(coords_by_bz.keys()))
    safe_to_disintegrate = set()
    for k in keys:
        for block in coords_by_bz[k]:
            is_supporting = False
            above_k = block[1][2] + 1
            for c in coords_by_bz[above_k]:
                overlap = x_y_overlap(block, c)
                print('supporting', block, c, overlap)
                if overlap:
                    supports = support_counts[c]
                    is_supporting = supports == 1
                if is_supporting:
                    break
            print('can remove', block, not is_supporting)
            if not is_supporting:
                count += 1
                safe_to_disintegrate.add(block)

    if part2:
        fall_count = 0
        for blocks in coords_by_bz.values():
            for block in blocks:
                if block not in safe_to_disintegrate:
                    b_fall_set = set()
                    q = set()
                    for c in supporting.get(block):
                        if len(supported_by.get(c)) == 1:
                            q.add(c)
                    while q:
                        n = q.pop()
                        b_fall_set.add(n)
                        for c in supporting.get(n, set()):
                            cs = supported_by.get(c)
                            if len(cs) < 2 or cs.issubset(b_fall_set):
                                q.add(c)
                    fall_count += len(b_fall_set)
                    print(block,len(b_fall_set))

        return fall_count
    else:
        return count


def x_y_overlap(block1, block2):
    b1_x1 = block1[0][0]
    b1_x2 = block1[1][0]
    b2_x1 = block2[0][0]
    b2_x2 = block2[1][0]
    x_overlap = b1_x1 in range(b2_x1, b2_x2 + 1) or b1_x2 in range(b2_x1, b2_x2 + 1) \
                or b2_x1 in range(b1_x1, b1_x2 + 1) or b2_x2 in range(b1_x1, b1_x2 + 1)
    if not x_overlap:
        return False
    b1_y1 = block1[0][1]
    b1_y2 = block1[1][1]
    b2_y1 = block2[0][1]
    b2_y2 = block2[1][1]
    y_overlap = b1_y1 in range(b2_y1, b2_y2 + 1) or b1_y2 in range(b2_y1, b2_y2 + 1) \
                or b2_y1 in range(b1_y1, b1_y2 + 1) or b2_y2 in range(b1_y1, b1_y2 + 1)
    if not y_overlap:
        return False
    return x_overlap and y_overlap


if __name__ == '__main__':
    # assert day22('day22_test.txt', False) == 5
    # assert day22('day22_test2.txt', False) == 1
    # assert day22('day22_input.txt', False) == 426

    assert day22('day22_test.txt', True) == 7
    assert day22('day22_input.txt', True) == 61920
