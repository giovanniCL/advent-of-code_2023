def transpose(pattern):
    transposed = []
    for j in range(len(pattern[0])):
        transposed_row = ""
        for row in pattern:
            transposed_row += row[j]
        transposed.append(transposed_row)
    return transposed

def rotate_clockwise(pattern):
    rotated = []
    row_len = len(pattern[0])
    for j in range(row_len):
        rotated_row = ""
        for row in pattern[::-1]:
            rotated_row += row[j]
        rotated.append(rotated_row)
    return rotated

def rotate_anticlockwise(pattern):
    rotated = []
    row_len = len(pattern[0])
    for j in range(row_len, 0, -1):
        rotated_row = []
        for row in pattern:
            rotated_row.append(row[j - 1])
        rotated.append(rotated_row)
    return rotated

def tilt_row(row):
    row_str = "".join(row)
    segments = row_str.split("#")
    new_row = []
    for segment in segments:
        if segment == "":
            new_row.append(segment)
        else:
            new_segment = "".join(sorted(segment, key=lambda x: 1 if x == "." else 0))
            new_row.append(new_segment)
    new_row = list("#".join(new_row))
    return new_row

def tilt(grid):
    tilted_grid = []
    for row in grid:
        tilted_grid.append(tilt_row(row))
    return tilted_grid

def cycle(grid):
    current = rotate_anticlockwise(grid)
    for _ in range(4):
        current = rotate_clockwise(tilt(current))
    return(rotate_clockwise(current))

def calculate_load(grid):
    total = 0
    for j, _ in enumerate(grid):
        total += sum([int(char == "O") * (len(grid) - j) for char in grid[j]])
    return total

def find_start_period_and_list(grid):
    grid_dict = {}
    grid_list = []
    for i in range(1000000000):
        grid_string = "\n".join(["".join(line) for line in grid])
        if grid_string in grid_dict.keys(): break
        grid_dict[grid_string] = i   
        grid_list.append(grid)     
        grid = cycle(grid)
    start = grid_dict[grid_string]
    period = i - start
    return i, period, grid_list

def part_1(grid):
    transposed_grid = transpose(grid)
    tilted_grid = tilt(transposed_grid)
    return calculate_load(transpose(tilted_grid))

def part_2(grid):
    start, period, grid_list = find_start_period_and_list(grid)
    magic_index = ((1000000000 - start) % period) + start
    for _ in range(magic_index):
        grid = cycle(grid)
    return calculate_load(grid)

def main():
    with open("input.txt", "r") as input_file:
        input_lines = input_file.readlines()
    grid = list(map(lambda x: list(x.strip()), input_lines))
    result_part_1 = part_1(grid)
    result_part_2 = part_2(grid)
    print(f"Load in first row after one tilt north: {result_part_1}")
    print(f"Load in first row after 1000000000 cycles: {result_part_2}")

if __name__ == "__main__":
    main()