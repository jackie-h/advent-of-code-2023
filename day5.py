def day5(filename):
    print('Day 5: If You Give A Seed A Fertilizer')

    res = 0
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
        res = solve(lines)
        print(res)
    return res


def solve(lines):
    res = None
    res2 = None

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
                print(numbers)
                s_maps.get(map_name).append(list(map(int, numbers)))

    print('seeds', seeds)
    print('maps', s_maps)

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

    print('Part 2')
    i = 0
    while i < len(seeds):
        seed_start = seeds[i]
        seed_range = seeds[i + 1]
        i = i + 2
        print('seed=', [seed_start, seed_range])
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
            if res2 is None:
                res2 = int(lr[0])
            else:
                res2 = min(res2, int(lr[0]))

    return res, res2


def get_value_ranges(ranges, values):
    valid_ranges = []
    intersected = []

    min_start = None
    for rg in ranges:
        start = rg[0]
        incr = rg[1]
        end = start + incr
        for row in values:
            source_start = row[1]
            rl = row[2]
            source_end = source_start + rl
            intersect = range_intersect(range(start, end), range(source_start, source_end))
            if min_start is None:
                min_start = start
            else:
                min_start = min(min_start, start)
            if intersect is not None:
                intersected.append(intersect)
                dest_start = row[0]
                s_offset = intersect.start - source_start
                ds = dest_start + s_offset
                r = intersect.stop - intersect.start
                valid_ranges.append([ds, r])
                # if start < intersect.start:
                #     valid_ranges.append([start,intersect.start - start])
                # if end > intersect.stop:
                #     valid_ranges.append([intersect.stop+1, end - intersect.stop])
        # remaining = [(start,end)]
        # for inter in intersected:
        #
        #     x = remaining[0] - inter


    if len(valid_ranges) == 0:
        valid_ranges = ranges
    else:
        min_inter_s = None

        for inter in intersected:
            if min_inter_s is None:
                min_inter_s = inter.start
            else:
                min_inter_s = min(min_inter_s,inter.start)
        if min_start < min_inter_s:
            valid_ranges.append([min_start, min_inter_s - min_start])
    print('intersected=', intersected)
    return valid_ranges


def range_intersect(r1, r2):
    return (range(max(r1.start,r2.start), min(r1.stop,r2.stop))) or None


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
    assert day5('day5_test.txt') == (35, 46)

    assert day5('day5_input.txt') == 403695602
