
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
        elif ':' in line:
            map_name = line.split(':')[0]
            s_maps[map_name] = []
        else:
            numbers = line.strip().split()
            if len(numbers) > 0:
                print(numbers)
                s_maps.get(map_name).append(numbers)

    print('seeds', seeds)
    print('maps', s_maps)

    for seed in seeds:
        soil = get_value(int(seed), s_maps.get('seed-to-soil map'))
        fertilizer = get_value(soil, s_maps.get('soil-to-fertilizer map'))
        water = get_value(fertilizer, s_maps.get('fertilizer-to-water map'))
        light = get_value(water, s_maps.get('water-to-light map'))
        temp = get_value(light, s_maps.get('light-to-temperature map'))
        humidity = get_value(temp, s_maps.get('temperature-to-humidity map'))
        location = get_value(humidity, s_maps.get('humidity-to-location map'))
        print(soil,fertilizer,water,light,temp,humidity)
        print('location', location)
        if res is None:
            res = location
        else:
            res = min(res,location)

    i = 0
    while i < len(seeds):
        seed_start = seeds[i]
        seed_range = seeds[i+1]
        i = i+2
        soil = get_value_ranges([[seed_start,seed_range]], s_maps.get('seed-to-soil map'))
        fertilizer = get_value_ranges(soil, s_maps.get('soil-to-fertilizer map'))
        water = get_value_ranges(fertilizer, s_maps.get('fertilizer-to-water map'))
        light = get_value_ranges(water, s_maps.get('water-to-light map'))
        temp = get_value_ranges(light, s_maps.get('light-to-temperature map'))
        humidity = get_value_ranges(temp, s_maps.get('temperature-to-humidity map'))
        locations = get_value_ranges(humidity, s_maps.get('humidity-to-location map'))
        print(soil,fertilizer,water,light,temp,humidity)
        print('location', locations)
        for lr in locations:
            if res2 is None:
                res2 = int(lr[0])
            else:
                res2 = min(res2,int(lr[0]))

    return res,res2

def get_value_ranges(ranges, values):
    valid_ranges = []
    for range in ranges:
        start = int(range[0])
        incr = int(range[1])
        end = start + incr
        for row in values:
            source_start = int(row[1])
            rl = int(row[2])
            source_end = source_start + rl
            dest_start = int(row[0])
            if (start < source_start and end > source_end):
                valid_ranges.append([dest_start, rl])
            elif (start >= source_start and start <= source_end):
                delta = int(start) - source_start
                valid_ranges.append([dest_start + delta, rl - delta])
            elif (end >= source_start and end <= source_end):
                valid_ranges.append([dest_start,min(end,source_end) - source_start])
    return valid_ranges

def get_value(input, values):
    for row in values:
        source_start = int(row[1])
        if input >= source_start:
            rl = int(row[2])
            source_end = source_start + rl
            if input <= source_end:
                dest_start = int(row[0])
                return dest_start + (input - source_start)
    return input

if __name__ == '__main__':
    assert day5('day5_test.txt') == (35,46)

    assert day5('day5_input.txt') == 403695602

