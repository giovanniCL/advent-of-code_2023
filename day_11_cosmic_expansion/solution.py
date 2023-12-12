from itertools import combinations

def get_rows_and_cols_expand(grid):
    rows_with_galaxies = set()
    cols_with_galaxies = set()
    for row, line in enumerate(grid):
        for col, space in enumerate(line):
            if space == "#":
                rows_with_galaxies.add(row)
                cols_with_galaxies.add(col)
    rows_to_expand = [*sorted(list(set(range(len(grid))) - rows_with_galaxies)), float("inf")]
    cols_to_expand = [*sorted(list(set(range(len(grid[0]))) - cols_with_galaxies)), float("inf")]
    return rows_to_expand, cols_to_expand

def get_galaxy_indices(grid):
    galaxy_indices = set()
    for row, line in enumerate(grid):
        for col, space in enumerate(line):
            if space == "#":
                galaxy_indices.add((row, col))
    return galaxy_indices


def get_empty_lines(grid, lines_to_expand):
    empty_lines = 0
    num_empty_lines_up_to_i = []
    for i in range(len(grid)):
        if i > lines_to_expand[empty_lines]:
            empty_lines += 1
        num_empty_lines_up_to_i.append(empty_lines)
    return num_empty_lines_up_to_i

def expand(row, col, num_empty_rows_up_to_i, num_empty_cols_up_to_i, expansion_offset):
    return (row + (num_empty_rows_up_to_i[row] * expansion_offset), col + (num_empty_cols_up_to_i[col] * expansion_offset))

def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def solution(galaxy_indices, num_empty_rows_up_to_i, num_empty_cols_up_to_i, expansion_offset):
    total = 0
    for galaxy_1, galaxy_2 in combinations(galaxy_indices, 2):
        expanded_1 = expand(*galaxy_1, num_empty_rows_up_to_i, num_empty_cols_up_to_i, expansion_offset)
        expanded_2 = expand(*galaxy_2, num_empty_rows_up_to_i, num_empty_cols_up_to_i, expansion_offset)
        total += distance(expanded_1, expanded_2)
    return total

def main():
    with open("input.txt") as input_file:
        input_lines = input_file.readlines()
    grid = [list(line.strip()) for line in input_lines]
    rows_to_expand, cols_to_expand = get_rows_and_cols_expand(grid)
    galaxy_indices = get_galaxy_indices(grid)
    num_empty_rows_up_to_i = get_empty_lines(grid, rows_to_expand)
    num_empty_cols_up_to_i = get_empty_lines(grid, cols_to_expand)
    solution_part_1 = solution(galaxy_indices, num_empty_rows_up_to_i, num_empty_cols_up_to_i, 1)
    solution_part_2 = solution(galaxy_indices, num_empty_rows_up_to_i, num_empty_cols_up_to_i, 999999)
    print(f"Total minimum distance between all galaxies with double expansion: {solution_part_1}")
    print(f"Total minimum distance between all galaxies with a million times expansion: {solution_part_2}")

if __name__ == "__main__":
    main()

