import math

def parse_input(input_lines):
    directions = list(input_lines[0].strip())
    directions.extend(list(input_lines[1].strip()))
    map = {}
    for line in input_lines[2:]:
        line_list = line.split("=")
        key = line_list[0].strip() 
        value = line_list[1].strip()[1:-1].split(",")
        value[1] = value[1].strip()
        map[key] = value
    return directions, map

def part_1(directions, map):
    count = 0
    current = "AAA"
    while current != "ZZZ":
        direction = directions[count % len(directions)]
        current = map[current][0 if direction == "L" else 1]
        count += 1
    return count

def part_2(directions, map):
    starting_points = [key for key in map.keys() if key[-1] == "A"]
    counts = []
    for starting_point in starting_points:
        count = 0
        current = starting_point
        while current[-1] != "Z":
            direction = directions[count % len(directions)]
            current = map[current][0 if direction == "L" else 1]
            count += 1
        counts.append(count)
    return math.lcm(*counts)

def main():
    with open("input.txt", "r") as input_file:
        input_lines = input_file.readlines()
    directions, map = parse_input(input_lines)
    result_part_1 = part_1(directions, map)
    result_part_2 = part_2(directions, map)
    print(f"Number of steps until destination: {result_part_1}")
    print(f"Number of steps until all destinations synced: {result_part_2}")

if __name__ == "__main__":
    main()