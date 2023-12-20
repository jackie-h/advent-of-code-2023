def day20(filename, part2):
    print('Day 20: Pulse Propagation')

    res = 0
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
        res = solve(lines, part2)
        print(res)

    return res


def solve(lines, part2):
    res = 0

    connections = {}
    for line in lines:
        name, tail = line.split(' -> ')
        ptype = ''
        if name.startswith('&') or name.startswith('%'):
            ptype = name[0:1]
            name = name[1:]
        conns = tail.split(', ')
        connections[name] = (ptype, conns)

    states = {}

    total = [0, 0]

    i = 0
    rx = False
    if part2:
        while not rx:
            i += 1
            print(i)
            rx, pulses = push(connections, states, part2)

    else:
        for i in range(0, 1000):
            rx, pulses = push(connections, states, part2)
            print(i, pulses, res)
            total[0] = total[0] + pulses[0]
            total[1] = total[1] + pulses[1]
        res = total[0] * total[1]

    if part2:
        return i
    else:
        return res


def push(connections, state, part2):
    next: list = connections['broadcaster'][1]
    pulse = 0
    prev = 'broadcaster'
    pulses = [1, 0]
    rx, pulses = move(connections, [(prev, pulse, next)], pulses, state, part2)

    return rx, pulses


def move(connections, move_blocks, pulses, state, part2):
    next = []
    rx = False
    for prev, pulse, moves in move_blocks:
        for n in moves:
            #print(prev, pulse, '->', n)
            pulses[pulse] += 1
            if part2 and n == 'rx':
                if pulse == 0:
                    rx = True
                    break

            if connections.get(n) is not None:
                type, x = connections[n]
                if type == '%':
                    if state.get(n) is None:
                        state[n] = 'off'
                    if pulse == 0:
                        if state[n] == 'off':
                            state[n] = 'on'
                            next.append((n, 1, x))
                        else:
                            state[n] = 'off'
                            next.append((n, 0, x))

                elif type == '&':
                    current = state.get(n)
                    if current is None:
                        current = {}
                        state[n] = current
                        for k, v in connections.items():
                            if n in v[1]:
                                current[k] = 0
                    current[prev] = pulse

                    if sum(current.values()) == len(current.keys()):
                        next.append((n, 0, x))
                    else:
                        next.append((n, 1, x))

    if len(next) > 0 and not rx:
        rx, pulses = move(connections, next, pulses, state, part2)
    return rx, pulses


if __name__ == '__main__':
    assert day20('day20_test.txt', False) == 32000000
    assert day20('day20_test2.txt', False) == 11687500
    assert day20('day20_input.txt', False) == 787056720
    assert day20('day20_input.txt', True) == 0
