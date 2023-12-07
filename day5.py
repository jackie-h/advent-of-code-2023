
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

    return res


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
    assert day5('day5_test.txt') == 35

    assert day5('day5_input.txt') == 403695602

