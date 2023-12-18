def parse_input(input_lines):
    grid = []
    for line in input_lines:
        grid.append(list(line.strip()))
    return grid

def get_full_number(grid, i, j):
    result = grid[i][j]
    offset = 1
    while j + offset < len(grid[0]):
        character = grid[i][j + offset]
        if not character.isdigit(): break
        result += character
        offset += 1
    prefix = ""
    offset = -1
    while j + offset >= 0:
        character = grid[i][j + offset]
        if not character.isdigit(): break
        prefix = character + prefix
        offset -= 1
    return int(prefix + result)
    

def check_adjacent_characters(grid, i, j):
    parts = set()
    for y in [-1, 0, 1]:
        new_i = i + y
        if new_i < 0 or new_i >= len(grid): continue
        for x in [-1, 0, 1]:
            new_j = j + x
            if new_j < 0 or new_j >= len(grid[0]): continue
            if grid[new_i][new_j].isdigit():
                parts.add(get_full_number(grid, new_i, new_j))
    return list(parts)


def part_1(grid):
    total = 0
    checked = set()
    for i, row in enumerate(grid):
        for j, character in enumerate(row):
            if character != "." and not character.isdigit():
                parts = check_adjacent_characters(grid, i, j)
                for part in parts:
                    if part not in checked:
                        total += part
    return total


def part_2(grid):
    total = 0
    for i, row in enumerate(grid):
        for j, character in enumerate(row):
            if character == "*":
                parts =check_adjacent_characters(grid, i, j)
                if len(parts) == 2:
                    total += parts[0] * parts[1]
    return total

def main():
    with open("input.txt", "r") as input_file:
        input_lines = input_file.readlines()
    grid = parse_input(input_lines)
    result_part_1 = part_1(grid)
    result_part_2 = part_2(grid)
    print(f"Sum of part numbers: {result_part_1}")
    print(f"Sum of gear ratios: {result_part_2}")

if __name__ == "__main__":
    main()
