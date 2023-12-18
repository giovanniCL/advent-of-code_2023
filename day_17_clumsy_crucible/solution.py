from heapq import heappush, heappop

DIRECTIONS = set([(0, 1), (0, -1), (1, 0), (-1, 0)])

class Node:
    def __init__(self, pos, dir, dist_straight, tent_dist, grid, parent=None):
        self.pos = pos
        self.dir = dir
        self.dist_straight = dist_straight
        self.tent_dist = tent_dist
        self.grid = grid
        self.parent = parent

    def get_neighbors(self, min_dist_straight, max_dist_straight):
        direction_singleton = set([(self.dir[0] * -1, self.dir[1] * -1)])
        possible_directions = DIRECTIONS - direction_singleton
        neighbors = []
        for d in possible_directions:
            if d == self.dir and self.dist_straight >= max_dist_straight:
                continue
            elif self.dir != (0,0) and d != self.dir and self.dist_straight < min_dist_straight:
                continue
            new_y, new_x = (self.pos[0] + d[0], self.pos[1] + d[1])
            if new_x < len(self.grid[0]) and new_x >= 0 and new_y < len(self.grid) and new_y >= 0:
                neighbors.append(((new_y, new_x), d))
        return neighbors
    
    def __lt__(self, other):
        return self.tent_dist < other.tent_dist
    
    def __hash__(self):
        return hash((self.pos, self.dir, self.dist_straight))
    
    def __eq__(self, other):
        return all([self.pos == other.pos, self.dir == other.dir, self.dist_straight == other.dist_straight])
    
def dijkstra(grid, min_dist_straight, max_dist_straight):
    traceback  = [[None for _ in row] for row in grid]
    start_node = Node((0,0), (0,0), 0, 0, grid)
    heap = [start_node]
    distances_from_start = {start_node: 0}
    visited = set()
    end_row, end_col = len(grid) - 1, len(grid[0]) - 1
    while len(heap) > 0:
        current = heappop(heap)
        if current.pos == (end_row, end_col): break
        if current in visited: continue
        visited.add(current)
        neighbors = current.get_neighbors(min_dist_straight, max_dist_straight)
        for (neighbor_row, neighbor_col), neighbor_dir in neighbors:
            dist_straight = current.dist_straight + 1 if neighbor_dir == current.dir else 1
            distance_from_start = grid[neighbor_row][neighbor_col] + distances_from_start.get(current, float("inf"))
            new_node = Node((neighbor_row, neighbor_col), neighbor_dir, dist_straight, distance_from_start, grid, parent=current)
            if distance_from_start  <= distances_from_start.get(new_node, float("inf")):
                distances_from_start[new_node] = distance_from_start
                traceback[neighbor_row][neighbor_col] = current
                heappush(heap, new_node)
    return distances_from_start[current]

def part_1(grid):
    return dijkstra(grid, 1, 3)

def part_2(grid):
    return dijkstra(grid, 4, 10)

def main():
    with open("input.txt", "r") as input_file:
        input_lines = input_file.readlines()
    grid = [list(map(int, list(line.strip()))) for line in input_lines]
    result_part_1 = part_1(grid)
    result_part_2 = part_2(grid)
    print(f"Minimum heat loss with top-heavy crucibles: {result_part_1}")
    print(f"Minimum heat loss with ultra crucibles: {result_part_2}")

if __name__ == "__main__":
    main()
