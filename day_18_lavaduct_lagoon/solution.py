DIRECTION_MAP = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, -1),
    "D": (0, 1)
}

def area(corners):
    #Shoelace Theorem
    total = 0
    for i, corner in enumerate(corners):
        next_corner = corners[(i + 1) % len(corners)]
        total += ((next_corner[0] - corner[0]) * (next_corner[1] + corner[1])) / 2
    return abs(total)

def num_lattices(area, num_edges):
    # revese Pick's theorem
    return area + 1 - (num_edges//2)

def first_columns_as_instructions(line):
    bearing, distance, _ = line
    return bearing, distance

def last_column_as_instruction(line):
    info = line[-1]
    distance = int(info[:-1], 16)
    bearing = "RDLU"[int(info[-1])]
    return bearing, distance

def get_shape_corners_and_num_edges(instructions, parsing_function):
    x, y = (0,0)
    corners = []
    num_edges = 0
    for instruction in instructions:
        bearing, distance = parsing_function(instruction)
        corners.append((x, y))
        num_edges += distance
        dx, dy = DIRECTION_MAP[bearing]
        x += dx * distance
        y += dy * distance
    return corners, num_edges

def get_volume_of_hole(corners, num_edges):
    return int(num_lattices(area(corners), num_edges) + num_edges)

def part_1(instructions):
    corners, num_edges = get_shape_corners_and_num_edges(instructions, first_columns_as_instructions)
    return get_volume_of_hole(corners, num_edges)

def part_2(instructions):
    corners, num_edges = get_shape_corners_and_num_edges(instructions, last_column_as_instruction)
    return get_volume_of_hole(corners, num_edges)

def main():
    with open("input.txt", "r") as input_file:
        input_lines = input_file.readlines()
    parsed_lines = [line.strip().split(" ") for line in input_lines]
    instructions = [[x, int(y), z[2:-1]] for x, y, z in parsed_lines]
    result_part_1 = part_1(instructions)
    result_part_2 = part_2(instructions)
    print(f"Cubic meters of lava after following first two columns of instructions: {result_part_1}")
    print(f"Cubic meters of lava after following last column of instructions: {result_part_2}")

if __name__ == "__main__":
    main()
