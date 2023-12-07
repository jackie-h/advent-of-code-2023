
def day4(filename):
    print('Day 4: Scratchcards')

    res = 0
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
        res = solve(lines)
        print(res)
    return res


def solve(lines):
    res = 0
    multipliers = [1] * len(lines)
    for i,line in enumerate(lines):
        tail = line.split(":")[1]
        winners = tail.split("|")[0].split()
        card = tail.split("|")[1].split()
        print(i, winners, card)
        ct = 0
        ws = 0
        for v in card:
            if v in winners:
                ws += 1
                if ct == 0:
                    ct = 1
                else:
                    ct = ct*2
        print(ct)
        print('winners count', ws)
        res = res + ct
        s = i + 1
        multiplier = multipliers[i]
        while s < (i + 1 + ws):
            val = multipliers[s] + multiplier
            multipliers[s] = val
            s += 1
        print('Multipliers', i, multipliers)
    print('Multipliers', multipliers)
    return res, sum(multipliers)


if __name__ == '__main__':
    assert day4('day4_test.txt') == (13,30)

    assert day4('day4_input.txt') == (24160, 5659035)