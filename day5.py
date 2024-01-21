def day5(filename, part2):
    print('Day 5: If You Give A Seed A Fertilizer')

    res = 0
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
        res = solve(lines, part2)
        print(res)
    return res


def solve(lines, part2):
    res = None

    s_maps = {}
    seeds = []
    map_name = ''
    for line in lines:
        if line.startswith("seeds:"):
            seeds = line.split(":")[1].split()
            seeds = list(map(int, seeds))
        elif ':' in line:
            map_name = line.split(':')[0]
            s_maps[map_name] = []
        else:
            numbers = line.strip().split()
            if len(numbers) > 0:
                #print(numbers)
                s_maps.get(map_name).append(list(map(int, numbers)))

    #print('seeds', seeds)
    #print('maps', s_maps)

    if not part2:
        for seed in seeds:
            soil = get_value(seed, s_maps.get('seed-to-soil map'))
            fertilizer = get_value(soil, s_maps.get('soil-to-fertilizer map'))
            water = get_value(fertilizer, s_maps.get('fertilizer-to-water map'))
            light = get_value(water, s_maps.get('water-to-light map'))
            temp = get_value(light, s_maps.get('light-to-temperature map'))
            humidity = get_value(temp, s_maps.get('temperature-to-humidity map'))
            location = get_value(humidity, s_maps.get('humidity-to-location map'))
            print(soil, fertilizer, water, light, temp, humidity)
            print('location', location)
            if res is None:
                res = location
            else:
                res = min(res, location)
    else:
        print('Part 2')
        i = 0
        while i < len(seeds):
            seed_start = seeds[i]
            seed_range = seeds[i + 1]
            i = i + 2

            print('seed=', range(seed_start, seed_start + seed_range))
            soil = get_value_ranges([[seed_start, seed_range]], s_maps.get('seed-to-soil map'))
            print('soil=', soil)
            fertilizer = get_value_ranges(soil, s_maps.get('soil-to-fertilizer map'))
            print('fertilizer=', fertilizer)
            water = get_value_ranges(fertilizer, s_maps.get('fertilizer-to-water map'))
            print('water=', water)
            light = get_value_ranges(water, s_maps.get('water-to-light map'))
            print('light=', light)
            temp = get_value_ranges(light, s_maps.get('light-to-temperature map'))
            print('temp=', temp)
            humidity = get_value_ranges(temp, s_maps.get('temperature-to-humidity map'))
            print('humidity=', humidity)
            locations = get_value_ranges(humidity, s_maps.get('humidity-to-location map'))
            print('location', locations)
            for lr in locations:
                if res is None:
                    res = int(lr[0])
                else:
                    res = min(res, int(lr[0]))

    return res


def get_value_ranges(input_ranges, values):
    valid_ranges = []

    for rg in input_ranges:
        intersected = []
        start = rg[0]
        incr = rg[1]
        end = start + incr
        ir = (start, end)
        for row in values:
            source_start = row[1]
            rl = row[2]
            source_end = source_start + rl
            rr = (source_start, source_end)
            intersect = range_intersect(ir, rr)

            if intersect is not None:
                print('Match', rr)
                intersected.append(intersect)
                dest_start = row[0]
                s_offset = intersect[0] - source_start
                ds = dest_start + s_offset
                r = intersect[1] - intersect[0]
                print('Matches', (ds, ds + r))
                valid_ranges.append((ds, r))

        print('intersected=', intersected)
        # find remaining gaps if exist
        remaining = [(start,end)]
        for i1 in intersected:
            new_r = []
            for a in remaining:
                diffs = range_diff(a, i1)
                print(diffs)
                for d in diffs:
                    new_r.append((d[0],d[1] - d[0]))
            remaining = new_r

        valid_ranges.extend(remaining)

    return valid_ranges


def range_intersect(r1, r2):
    r = range(max(r1[0],r2[0]), min(r1[1],r2[1])) or None
    if r is not None:
        return r.start, r.stop
    return r


def range_diff(r1, r2):
    s1, e1 = r1
    s2, e2 = r2
    endpoints = sorted((s1, s2, e1+1, e2+1))
    result = []
    if endpoints[0] == s1 and endpoints[1] != s1:
        result.append((endpoints[0], endpoints[1] - 1))
    if endpoints[3] == e1 and endpoints[2] != e1:
        result.append((endpoints[2], endpoints[3] - 1))
    return result


def get_value(input, values):
    for row in values:
        source_start = row[1]
        if input >= source_start:
            rl = row[2]
            source_end = source_start + rl
            if input <= source_end:
                dest_start = row[0]
                return dest_start + (input - source_start)
    return input


if __name__ == '__main__':
    #assert day5('day5_test.txt', False) == 35
    #assert day5('day5_test.txt', True) == 46
    #assert day5('day5_input.txt', False) == 403695602
    assert day5('day5_input.txt', True) == 0
