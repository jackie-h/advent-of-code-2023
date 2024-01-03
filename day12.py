from itertools import combinations


def day12(filename):
    print('Day 12: Hot Springs')

    res = 0
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
        res = solve(lines)
        print(res)

    return res


def solve(lines):
    res = 0
    for line in lines:
        #print(line)
        row,tail = line.split()
        values = list(map(int, tail.split(',')))
        group_count = len(values)
        n_empty = len(row) - sum(values)

        #Only one solution
        if n_empty == (group_count - 1):
            res += 1
            continue

        else:
            ranges = range(len(row) - values[len(values) - 1] + 1)#range(group_count + n_empty)
            indexes = []
            for r in ranges:
                if row[r] != '.':
                    indexes.append(r)

            valid = []
            for p in combinations(indexes, group_count):
                ok = True

                for i in range(0,len(p)):
                    c_i = p[i]

                    prev_i = 0
                    prev_v = 0

                    if i > 0:
                        prev_i = p[i-1]
                        prev_v = values[i-1]
                        if c_i < (prev_i + prev_v + 1):
                            ok = False
                            break

                    if (i == len(row) and c_i + values[i] > len(row))\
                            or row[c_i:c_i + values[i]].find('.') > -1\
                            or row[c_i - 1].find('#') > -1\
                            or (c_i + values[i] < len(row) and row[c_i + values[i]].find('#') > -1)\
                            or i == len(p) - 1 and row[c_i + values[i]:].find('#') > -1\
                            or row[prev_i + prev_v:c_i].find('#') > -1:
                        ok = False
                        break

                if ok:
                    valid.append(p)
                    res += 1

                #print(p, ok)

            print(len(valid), line, valid)


    return res


if __name__ == '__main__':

    #assert day12('day12_test.txt') == 21
    assert day12('day12_input.txt') == 21

