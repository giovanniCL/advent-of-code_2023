class Beam:
    energized = set()
    global_path = set()
    beams = []
    rotation_mapping = {
        "/":{
            (1, 0): (0, -1),
            (-1, 0): (0, 1),
            (0, 1): (-1, 0),
            (0, -1): (1, 0)
        },
        "\\":{
            (1, 0): (0, 1),
            (-1, 0): (0, -1),
            (0, 1): (1, 0),
            (0, -1): (-1, 0)
        }
    }
    def __init__(self, pos, dir, grid, path=None):
        self.pos = pos
        self.dir = dir
        self.grid = grid
        self.path = [] if not path else path
        Beam.beams.append(self)

    def shine(self):
        x, y = self.pos
        x_dir, y_dir = self.dir
        new_x = x + x_dir
        new_y = y + y_dir
        if (new_x >= 0 and new_x < len(self.grid[0]) and new_y >= 0 and new_y < len(self.grid)) and ((new_x, new_y), self.dir) not in Beam.global_path:
            self.pos = (new_x, new_y)
            self.path.append(((self.pos), (self.dir)))
            Beam.global_path.add(((self.pos), (self.dir)))
            return True
        return False

    def rotate(self, character):
        self.dir = Beam.rotation_mapping[character][self.dir]

    def split(self, character):
        if character == "|" and self.dir[0] != 0:
            Beam(self.pos, (0, 1), self.grid, self.path.copy())
            self.dir = (0, -1)
        if character == "-" and self.dir[1] != 0:
            Beam(self.pos, (1, 0), self.grid, self.path.copy())
            self.dir = (-1, 0)
    
    def update(self):
        Beam.energized.add(self.pos)
        character = self.grid[self.pos[1]][self.pos[0]]
        if character in "/\\":
            self.rotate(character)
        elif character in "|-":
            self.split(character)
        shone = self.shine()
        if not shone:
            return False
        return True
    
    @classmethod
    def reset(cls):
        cls.energized = set()
        cls.global_path = set()
        cls.beams = []

def display_energized_grid(grid):
    grid_copy = [line.copy() for line in grid]
    for x, y in Beam.energized:
        if grid_copy[y][x] == ".":
            grid_copy[y][x] = "#"
    print("\n".join(["".join(line) for line in grid_copy]))
    
def find_num_energized(start, direction, grid):
    Beam.reset()
    Beam(start, direction, grid)
    while len(Beam.beams) > 0:
        beam = Beam.beams.pop(0)
        updated = beam.update()
        if updated: Beam.beams.append(beam)
    return len(Beam.energized)

def part_1(grid):
    return find_num_energized((0,0), (1,0), grid)

def part_2(grid):
    left_entrypoints = [(0, i) for i in range(len(grid))]
    right_entrypoints = [(len(grid[0]) - 1, i) for i in range(len(grid))]
    top_entrypoints = [(j, 0) for j in range(len(grid[0]))]
    bottom_entrypoints = [(j, len(grid) - 1) for j in range(len(grid[0]))]

    entry_config =\
    [
        (left_entrypoints, (1, 0)),
        (right_entrypoints, (-1, 0)), 
        (top_entrypoints, (0, 1)),
        (bottom_entrypoints, (0, -1))
    ]
    energized = []
    for entry_points, direction in entry_config:
        for entry_point in entry_points:
            energized.append(find_num_energized(entry_point, direction, grid))
    return max(energized)

def main():
    with open("input.txt", "r") as input_file:
        input_lines = input_file.readlines()
    grid = [list(line.strip()) for line in input_lines]
    result_part_1 = part_1(grid)
    result_part_2 = part_2(grid)
    print(f"Number of beams energized from top left to right: {result_part_1}")
    print(f"Maximum number of beams energized across all entry points and directions: {result_part_2}")

if __name__ == "__main__":
    main()