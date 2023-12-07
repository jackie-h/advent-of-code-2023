import functools


def day7(filename,joker):
    print('Day 7: Camel Cards')

    res = 0
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
        res = solve(lines,joker)
        print(res)

    return res

def solve(lines,joker):
    res = 0
    input = []
    for line in lines:
        hand,bid = line.split()
        if joker:
            hand = hand.replace('J', '*')
        input.append((hand,bid))

    input = sorted(input, key=functools.cmp_to_key(compare))

    print(input)
    for i,hb in enumerate(input):
        h,b=hb
        res += (i+1)*int(b)

    return res


def compare(i1, i2):
    hand1, b1 = i1
    hand2, b2 = i2
    score1 = rank(hand1)
    score2 = rank(hand2)
    print(hand1, score1, hand2, score2)
    if score1 > score2:
        return 1
    elif score1 == score2:
        for c1,c2 in zip(hand1,hand2):
            s1 = char_score(c1)
            s2 = char_score(c2)
            if s1 > s2:
                return 1
            elif s1 < s2:
                return -1
        return 0
    else:
        return -1

def char_score(c):
    if c == 'A':
        return 14
    elif c == 'K':
        return 13
    elif c == 'Q':
        return 12
    elif c == 'J':
        return 11
    elif c == 'T':
        return 10
    elif c == '*':
        return 1
    else:
        return int(c)

def rank(hand):
    counts = {}
    joker_max = 0

    for c in hand:
        if c == '*':
            joker_max += 1
        else:
            if counts.get(c):
                counts[c] = counts.get(c) + 1
            else:
                counts[c] = 1

    max = 0

    for k, co in counts.items():
        if co > max:
            max = co

    max = max + joker_max

    if max == 5:
        return 7
    elif max == 4:
        return 6
    elif max == 3:
        if len(counts.keys()) == 2:
            return 5
        else:
            return 4
    elif max == 2:
        if len(counts.keys()) == 3:
            return 3
        else:
            return 2
    elif max == 1:
        if len(counts.keys()) == 5:
            return 1
        else:
            return 0
    else:
        return 0


if __name__ == '__main__':
    assert day7('day7_test.txt', False) == 6440
    assert day7('day7_test.txt', True) == 5905

    assert day7('day7_input.txt', False) == 250370104
    assert day7('day7_input.txt', True) == 251735672