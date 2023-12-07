
def day4(filename):
    print('Day 4: Scratchcards')

    res = 0
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
        res = solve(lines)
    return res


def solve(lines):
    res = 0
    multipiers = [1] * len(lines)
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
        s = i
        while s < ws:
            val = multipiers[s] + 1
            multipiers[s] = val
            s += 1
    print(res)
    return res


if __name__ == '__main__':
    assert day4('day4_test.txt') == 13

    #assert day4('day4_input.txt') == 24160