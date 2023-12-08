

def day8(filename):
    print('Day 8: Haunted Wasteland')

    res = 0
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
        res = solve(lines)
        print(res)

    return res

def solve(lines):
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

    key = 'AAA'
    steps = 0
    while key != 'ZZZ':
        key,steps = follow_path(instruction, key, map, steps)

    return steps


def follow_path(instruction, key, map, steps):
    for s in instruction:
        steps += 1
        l, r = map.get(key)
        if s == 'L':
            key = l
        elif s == 'R':
            key = r
        if key == 'ZZZ':
            break
    return key,steps

if __name__ == '__main__':
    assert day8('day8_test1.txt') == 2
    assert day8('day8_test2.txt') == 6
    assert day8('day8_input.txt') == 12737