from itertools import combinations
from functools import cache

def parse_input(input_lines):
    patterns = []
    current_pattern = []
    for line in input_lines:
        if line == "\n":
            patterns.append(current_pattern)
            current_pattern = []
        else: current_pattern.append(line.strip())
    patterns.append(current_pattern)
    return patterns

def insert_into_map(key, value, map):
    if key in map.keys():
        map[key].add(value)
    else: map[key] = set([value])

def get_mirror_front_candiates(map):
    candidates = []
    for value in map.values():
        if len(value) > 1:
            for a, b in combinations(value, 2):
                if abs(a - b) == 1: candidates.append((a, b))
    return candidates

@cache
def diff(line_1, line_2):
    return sum([int(char_1 != char_2) for char_1, char_2 in zip(line_1, line_2)])

@cache
def equals_or_diff_1(line_1, line_2):
    return diff(line_1, line_2) < 2

def transpose(pattern):
    transposed = []
    for j in range(len(pattern[0])):
        transposed_row = ""
        for row in pattern:
            transposed_row += row[j]
        transposed.append(transposed_row)
    return transposed

def aggregate_map_keys(map):
    key_pairs = [set([key_1, key_2]) for key_1, key_2 in combinations(map.keys(), 2) if equals_or_diff_1(key_1, key_2)]
    key_pairs.extend([set([key]) for key in map.keys()])
    new_keys = key_pairs
    new_map = {frozenset(key): set() for key in new_keys}
    for key, value in map.items():
        for new_key in new_map.keys():
            if key in new_key:
                new_map[new_key] = new_map[new_key].union(value)
    return new_map

def check_for_mirrors(pattern):
    row_map = {}
    for i, row in enumerate(pattern):
        insert_into_map(row, i, row_map)
    mirror_front_candidates = get_mirror_front_candiates(row_map)
    found = True
    current_mirror_index = -1
    for value in mirror_front_candidates:
        top = min(value[1], value[0])
        bottom = max(value[1], value[0])
        current_mirror_index = bottom
        while top >= 0 and bottom < len(pattern):
            if pattern[top] != pattern[bottom]:
                found = False
                break
            top -= 1
            bottom += 1
        if found: return current_mirror_index
        found = True
    return -1

def check_for_smudged_mirrors(pattern):
    row_map = {}
    for i, row in enumerate(pattern):
        insert_into_map(row, i, row_map)
    row_map = aggregate_map_keys(row_map)
    mirror_front_candidates = get_mirror_front_candiates(row_map)
    found = True
    current_mirror_index = -1
    for value in mirror_front_candidates:
        top = min(value[1], value[0])
        bottom = max(value[1], value[0])
        current_mirror_index = bottom
        diff_count = 0
        while top >= 0 and bottom < len(pattern):
            if not equals_or_diff_1(pattern[top], pattern[bottom]):
                found = False
                break
            curr_diff = int(pattern[top] != pattern[bottom])
            diff_count += curr_diff
            if diff_count > 1:
                found = False
                break
            top -= 1
            bottom += 1
        if diff_count == 0:
            found = True
            continue
        if found: return current_mirror_index
        found = True
    return -1


def solve(patterns, checking_function):
    total = 0
    for pattern in patterns:
        mirror_index = checking_function(pattern)
        multiplier = 100
        if mirror_index == -1:
            mirror_index = checking_function(transpose(pattern))
            multiplier = 1
        total += mirror_index * multiplier
    return total

def part_1(patterns):
    return solve(patterns, check_for_mirrors)

def part_2(patterns):
    return solve(patterns, check_for_smudged_mirrors)

def main():
    with open("input.txt", "r") as input_file:
        input_lines = input_file.readlines()
    patterns = parse_input(input_lines)
    result_part_1 = part_1(patterns)
    result_part_2 = part_2(patterns)
    print(f"Number resulting from summary of mirrors: {result_part_1}")
    print(f"Number resulting from summary of smudged mirrors: {result_part_2}")

if __name__ == "__main__":
    main()


    

    