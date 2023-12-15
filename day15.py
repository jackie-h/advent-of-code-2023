
def day15(filename, part2):
    print('Day 15: Lens Library')

    res = 0
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
        res = solve(lines, part2)
        print(res)

    return res


def solve(lines, part2):
    res = 0

    values = lines[0].split(',')

    if not part2:
        for value in values:
            cv = hash_it(value)
            print(value, cv)
            res += cv
    else:
        boxes = {}
        for value in values:

            if value.find('=') > 0:
                code,q = value.split("=")
                h = hash_it(code)

                if boxes.get(h) is None:
                    boxes[h] = {}
                b = boxes[h]
                b[code] = q
            else:
                code,q = value.split('-')
                h = hash_it(code)
                if boxes.get(h) is None:
                    boxes[h] = {}
                b = boxes[h]
                if b.get(code) is not None:
                    del b[code]

            print(boxes)

        #One plus the box number of the lens in question.
        #The slot number of the lens within the box: 1 for the first lens, 2 for the second lens, and so on.
        #The focal length of the lens.
        for k,v in boxes.items():
            a = k + 1
            for i,k in enumerate(v.keys()):
                b = i + 1
                c = v.get(k)
                res += a * b * int(c)

    return res


def hash_it(value):
    cv = 0
    for c in value:
        ascii = ord(c)
        cv += ascii
        cv = cv * 17
        cv = cv % 256
    return cv


if __name__ == '__main__':
    assert day15('day15_test.txt', False) == 1320
    assert day15('day15_input.txt', False) == 501680
    assert day15('day15_test.txt', True) == 145
    assert day15('day15_input.txt', True) == 241094


