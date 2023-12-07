def get_map(chunk):
    result = list(map(lambda x: list(map(int, x.strip().split(" "))),chunk.split("\n")[1:]))
    result.sort(key=lambda x: x[1])
    return result

def parse_input(input_text):
    chunks = input_text.split("\n\n")
    seeds = list(map(int, chunks[0].split(":")[1].strip().split(" ")))
    maps = list(map(get_map, chunks[1:]))
    return seeds, maps

def get_seed_ranges(seeds):
    return [range(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]

def get_value_from_map(key, map):
    map_len = len(map)
    high = map_len
    low = 0
    while low < high:
        mid = (high + low) // 2
        row = map[mid]
        source_range = range(row[1], row[1] + row[2])
        if key in source_range:
            return row[0] + (key - row[1])
        elif key > row[1]:
            low = mid + 1
        elif key < row[1]:
            high = mid - 1
    if low >= 0 and low < map_len and key in range(map[low][1], map[low][1] + map[low][2]):
        return map[low][0] + (key - map[low][1]) 
    return key

def get_value_from_map_reversed(key, map):
    for row in map:
        valid = True
        source_range = range(row[0], row[0] + row[2])
        destination_range = range(row[1], row[1] + row[2])
        if key in source_range:
            return row[1] + (key - row[0])
        elif key in destination_range:
            valid = False
    if valid: return key
    return None

def get_location_mins(interval, map_index, maps):
    map = maps[map_index]
    map.sort(key=lambda x: x[1])
    location_mins = []
    low = interval.start
    upper_limit = interval[-1]
    row_i = 0
    while low < upper_limit and row_i < len(map):
        row = map[row_i]
        possible_range = range(row[1], row[1] + row[2])
        found = True
        if low in possible_range:
            # if we find a mapping for the lower bound
            mapped_low = row[0] + (low - row[1])
            if interval[-1] in possible_range: high = interval[-1] + 1 # mapping for higher bound: all is good
            else: high = possible_range[-1] + 1 # no mapping for higher bound: make upper bound of mapping new upper bound
            row_i += 1
            mapped_high = row[0] + (high - row[1])
            low = high
        elif low < possible_range.start:
            # if lower bound is lower than start of the current mapping it means lower bound is not in this map
            mapped_low = low
            if interval[-1] in possible_range:
                # if upper bound is in this map: make start of current mapping the new upper nound
                high = possible_range.start
                mapped_high = row[0] + (high - row[1])
            else:
                # else all is good
                high = interval[-1] + 1
                mapped_high = high
            low = high
        else:
            # if lower bound is higher than current mapping upper bound
            # we dont know if we made find it in the future so we just go to the next row
            row_i += 1
            found = False # this boolean indicates we are not making a mapping in this iteration
        if found:
            if map_index == len(maps) - 1:
                location_mins.append(mapped_low)
            else:
                location_mins.extend(get_location_mins(range(mapped_low, mapped_high), map_index + 1, maps))
    if low < upper_limit:
        if map_index == len(maps) - 1: location_mins.append(low)
        else: location_mins.extend(get_location_mins(range(low, upper_limit), map_index + 1, maps))
    return location_mins

def part_1(seeds, maps):
    locations = []
    for seed in seeds:
        key = seed
        for map in maps:
            key = get_value_from_map(key, map)
        locations.append(key)
    return min(locations)

def part_2(seed_ranges, maps):
    location_mins = []
    for interval in seed_ranges:
        location_mins.extend(get_location_mins(interval, 0, maps))
    location_mins.sort()
    print(location_mins)
    for location in location_mins:
        key = location
        for map in maps[::-1]:
            key = get_value_from_map_reversed(key, map)
        for seed_range in seed_ranges:
            if key in seed_range:
                return location

def main():
    with open("input.txt") as input_file:
        input_text = input_file.read()
    seeds, maps = parse_input(input_text)
    seed_ranges = get_seed_ranges(seeds)
    result_part_1 = part_1(seeds, maps)
    result_part_2 = part_2(seed_ranges, maps)
    print(f"Minimum location number for seeds: {result_part_1}")
    print(f"Minimum location number for seed ranges: {result_part_2}")

if __name__ == "__main__":
    main()  
                