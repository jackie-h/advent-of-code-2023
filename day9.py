def day9(filename):
    print('Day 9: Mirage Maintenance')

    res = 0
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
        res = solve(lines)
        print(res)

    return res


def solve(lines):
    res = 0
    res2 = 0

    for line in lines:
        seqs = []
        first_seq = line.split()
        seqs.append(list(map(int, first_seq)))

        all_zero = False
        while not all_zero:
            all_zero = True
            seq = seqs[len(seqs) - 1]
            diffs = []
            for i in range(0, len(seq) - 1, 1):
                diff = seq[i+1] - seq[i]
                diffs.append(diff)
                all_zero = all_zero and diff == 0
            seqs.append(diffs)
        print(seqs)

        last = 0
        first = 0
        for i in reversed(range(1, len(seqs) - 1, 1)):
            print('i',i)
            l = seqs[i][len(seqs[i]) - 1]
            v1 = seqs[i-1][len(seqs[i-1]) - 1]
            last = v1 + l
            seqs[i - 1].append(last)
            f = seqs[i][0]
            f1 = seqs[i-1][0]
            first = f1 - f
            seqs[i - 1].insert(0,first)
            print(seqs)
        print(first, last)
        res += last
        res2 += first
    return res,res2


if __name__ == '__main__':
    assert day9('day9_test.txt') == (114, 2)
    assert day9('day9_input.txt') == (2043677056, 1062)