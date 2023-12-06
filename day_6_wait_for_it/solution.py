import re

def parse_input(input_lines):
    times = list(map(int, re.split(r"\s+",input_lines[0].split(":")[1].strip())))
    distances = list(map(int, re.split(r"\s+",input_lines[1].split(":")[1].strip())))
    time = int("".join([str(number) for number in times]))
    distance = int("".join([str(number) for number in distances]))
    return times, distances, time, distance

def get_number_of_wins(time, distance):
    speed = 0
    count = 0
    while speed <= time:
        new_distance = (time - speed) * speed
        if new_distance > distance:
            count += 1
        speed += 1
    return count

def part_1(times, distances):
    total = 1
    for time, distance in zip(times, distances):
        count = get_number_of_wins(time, distance)
        total *= count
    return total

def part_2(time, distance):
    return get_number_of_wins(time, distance)

def main():
    with open("input.txt", "r") as input_file:
        input_lines = input_file.readlines()
    times, distances, time, distance = parse_input(input_lines)
    result_part_1 = part_1(times, distances)
    result_part_2 = part_2(time, distance)
    print(f"Product of numbers of wins for each race: {result_part_1}")
    print(f"Number of wins for one big race: {result_part_2}")

if __name__ == "__main__":
    main()