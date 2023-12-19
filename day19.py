import collections

def day19(filename, part2):
    print('Day 19: Aplenty')

    res = 0
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
        res = solve(lines, part2)
        print(res)

    return res


def solve(lines, part2):
    res = 0

    rules = {}
    inputs = []
    for line in lines:

        if line.startswith('{'):
            vals = line.replace('{','').replace('}','').split(',')
            di = {}
            for val in vals:
                l,n = val.split('=')
                di[l] = int(n)
            inputs.append(di)
        elif line != '':
            key,tail = line.split('{')
            parts = tail.replace('}','').split(',')
            exp = []
            for part in parts:
                sexp = part.split(':')
                k = sexp.pop()
                rexp = None
                if len(sexp) == 1:
                    e = sexp[0]
                    if e.find('<') or e.find('>'):
                        c = e[0]
                        g = e[1]
                        r = int(e[2:])
                        rexp = (c,g,r)
                e = {k: rexp}
                exp.append(e)

            rules[key] = exp

    for i in inputs:
        rl = rules['in']
        ar = run_rule(i, rl, rules)
        print(i,ar)
        if ar == 'A':
            for v in i.values():
                res += v

    return res


def run_rule(i, rl, rules):
    for rc in rl:
        for ek, ee in rc.items():
            if ee is None:
                return check_result(i, ek, rules)
            else:
                l, g, v = ee
                iv = i[l]
                if g == '<':
                    if iv < v:
                        return check_result(i, ek, rules)
                    else:
                        break
                elif g == '>':
                    if iv > v:
                        return check_result(i, ek, rules)
                    else:
                        break


def check_result(i, ek, rules):
    if ek == 'A' or ek == 'R':
        return ek
    else:
        nr = rules[ek]
        if nr is not None:
            print('->', ek)
            return run_rule(i, nr, rules)
        else:
            return


if __name__ == '__main__':
    assert day19('day19_test.txt', False) == 19114
    assert day19('day19_input.txt', False) == 319295
