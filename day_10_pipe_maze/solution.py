from utils import character_direction_mapping, start_pipe_mapping

def find_start(grid):
    for row, line in enumerate(grid):
        col = line.find("S")
        if col != -1: return(row, col)

def get_loop(grid, start_row, start_col):
    for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        current = (start_row + direction[0], start_col + direction[1])
        loop = [current]
        old_direction = direction
        while True:
            direction_mapping = character_direction_mapping.get(grid[current[0]][current[1]])
            if direction_mapping is None:
                break
            new_direction = direction_mapping.get(old_direction)
            if new_direction is None:
                break
            current = (current[0] + new_direction[0], current[1] + new_direction[1])
            if current[0] < 0 or current[0] >= len(grid) or current[1] < 0 or current[1] >= len(grid[0]):
                break 
            old_direction = new_direction
            loop.append(current)
            if grid[current[0]][current[1]] == "S":
                return loop
            
def get_end_direction(loop):
    return (loop[-1][0] - loop[-2][0], loop[-1][1] - loop[-2][1])

def get_start_direction(loop):
    return (loop[0][0] - loop[-1][0], loop[0][1] - loop[-1][1])

def replace_s(grid, row, column, start_direction, end_direction):
    new_grid = [list(line) for line in grid]
    new_grid[row][column] = start_pipe_mapping[end_direction][start_direction]
    return new_grid

def part_1(loop):
    return len(loop)//2

def part_2(grid, loop):
    end_direction = get_end_direction(loop)
    start_direction = get_start_direction(loop)
    start_row, start_col = loop[-1]
    grid = replace_s(grid, start_row, start_col, start_direction, end_direction)
    inside_loop = set()
    for row, line in enumerate(grid):
        inside = False
        for col, character in enumerate(line):
            if (row, col) in loop:
                if character in "|JL":
                    inside = not inside
            elif inside:
                inside_loop.add((row, col))
    return len(inside_loop)

def main():
    with open("input.txt", "r") as input_file:
        input_lines = input_file.readlines()
    grid = [line.strip() for line in input_lines]
    start_row, start_col = find_start(grid)
    loop = get_loop(grid, start_row, start_col)
    solution_part_1 = part_1(loop)
    solution_part_2 = part_2(grid, loop)
    print(f"Distance in loop farthest away from start: {solution_part_1}")
    print(f"Number of tiles enclosed by loop: {solution_part_2}")

if __name__ == "__main__":
    main()