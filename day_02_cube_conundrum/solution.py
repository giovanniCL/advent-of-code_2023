from functools import reduce

CUBE_CONFIG = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def parse_input(input_lines):
    games = []
    for line in input_lines:
        id_part, sets_part = line.strip().split(":")
        game_id = int(id_part.strip().split(" ")[1])
        unparsed_sets = sets_part.strip().split(";")
        parsed_sets = []
        for unparsed_set in unparsed_sets:
            cube_list = unparsed_set.strip().split(",")
            parsed_set = {}
            for cube in cube_list:
                quantity, color = cube.strip().split(" ")
                parsed_set[color] = int(quantity)
            parsed_sets.append(parsed_set)
        game = {
            "id": game_id,
            "sets": parsed_sets
        }
        games.append(game)
    return games

def part_1(games):
    total = 0
    for game in games:
        possible = True
        for parsed_set in game["sets"]:
            for color, quantity in parsed_set.items():
                if int(quantity) > CUBE_CONFIG[color]:
                    possible = False
                    break
            if not possible: break
        if possible: total += game["id"]
    return total

def part_2(games):
    total = 0
    for game in games:
        max_quantities = {
            "red": 0,
            "blue": 0,
            "green": 0
        }
        for parsed_set in game["sets"]:
            for color, quantity in parsed_set.items():
                max_quantities[color] = max(max_quantities[color], quantity)
        power = reduce(lambda x, y: x * y,max_quantities.values())
        total += power
    return total

def main():
    with open("input.txt", "r") as input_file:
        input_lines = input_file.readlines()
    games = parse_input(input_lines)
    result_part_1 = part_1(games)
    result_part_2 = part_2(games)
    print(f"Sum of possible game IDs: {result_part_1}")
    print(f"Sum of the power of sets with minimum cubes: {result_part_2}")

if __name__ == "__main__":
    main()
    
        
