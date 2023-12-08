

def day8(filename, part2):
    print('Day 8: Haunted Wasteland')

    res = 0
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
        res = solve(lines, part2)
        print(res)

    return res


def solve(lines, part2):
    instruction = lines[0]
    map = {}

    for line in lines:
        if '=' in line:
            h,t = line.split("=")
            key = h.strip()
            l,r = t.split(",")
            lv = l.replace("(","").strip()
            rv = r.replace(")","").strip()
            map[key] = (lv,rv)
    print(map)

    steps = 0
    if not part2:
        key = 'AAA'
        while key != 'ZZZ':
            key,steps = follow_path(instruction, key, map, steps)
    else:
        # Part 2
        keys = [k for k in map.keys() if k.endswith('A')]
        print(keys)
        more = True

        while more:
            for s in instruction:
                steps += 1
                for i,key in enumerate(keys):
                    key = follow_step(s, key, map)
                    keys[i] = key

                print(steps, keys)
                stop = True
                for k in keys:
                    if not k.endswith('Z'):
                        stop = False
                        break
                if stop:
                    more = False
                    break

    return steps


def follow_path(instruction, key, map, steps):
    for s in instruction:
        steps += 1
        key = follow_step(s, key, map)
        if key == 'ZZZ':
            break
    return key,steps


def follow_step(s, key, map):
    l, r = map.get(key)
    if s == 'L':
        key = l
    elif s == 'R':
        key = r
    return key


if __name__ == '__main__':
    #assert day8('day8_test1.txt', False) == 2
    #assert day8('day8_test2.txt', False) == 6
    #assert day8('day8_test3.txt', True) == 6

    #assert day8('day8_input.txt', False) == 12737
    assert day8('day8_input.txt', True) == 12737
