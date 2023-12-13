import re

def parse_input(input_lines):
    spring_list = []
    number_list = []
    for line in input_lines:
        springs, numbers = line.split(" ")
        springs = list(springs.strip())
        numbers = list(map(int, numbers.strip().split(",")))
        spring_list.append(springs)
        number_list.append(numbers)
    return spring_list, number_list

def unfold(spring_list, number_list):
    unfolded_spring_list = []
    unfolded_number_list = []
    for springs, numbers in zip(spring_list, number_list):
        unfolded_spring_list.append((list("".join(springs) + "?") * 5)[:-1])
        unfolded_number_list.append(numbers * 5)
    return unfolded_spring_list, unfolded_number_list

def validate(springs, numbers):
    damaged_groups = [group for group in re.split(r"\.+","".join(springs).strip()) if group != ""]
    if len(damaged_groups) != len(numbers): return 0
    for i, number in enumerate(numbers):
        if len(damaged_groups[i]) != number: return 0
    return 1

def partial_validate(springs, numbers):
    damaged_groups = [group for group in re.split(r"\.+","".join(springs).strip()) if group != ""]
    if len(damaged_groups) == 0: return 1
    if len(damaged_groups) > len(numbers): return 0
    for i, group in enumerate(damaged_groups[:-1]):
        if len(group) != numbers[i]:
            return 0
    if len(damaged_groups[len(damaged_groups) - 1]) <= numbers[len(damaged_groups) - 1]:
        return 1
    else:
        return 0

memo = {}
def f(springs, numbers, i):
    if (tuple(springs), tuple(numbers), i) in memo.keys():
        return memo[(tuple(springs), tuple(numbers), i)]
    if i == len(springs): return validate(springs, numbers)
    prefix = springs[:i]
    if not partial_validate(prefix, numbers): return 0
    if springs[i] != "?": return f(springs, numbers, i + 1)
    total = 0
    for character in "#.":
        springs[i] = character
        total += f(springs, numbers, i + 1)
    springs[i] = "?"
    memo[(tuple(springs), tuple(numbers), i)] = total
    return total

def solve(spring_list, number_list):
    total = 0
    for springs, numbers in zip(spring_list, number_list):
        total += f(springs, numbers, 0)
    return total

def part_1(spring_list, number_list):
    return solve(spring_list, number_list)

def part_2(spring_list, number_list):
    return solve(*unfold(spring_list, number_list))

def main():
    with open("input.txt", "r") as input_file:
        input_lines = input_file.readlines()
    spring_list, number_list = parse_input(input_lines)
    spring_list_copy = [springs.copy() for springs in spring_list]
    result_part_1 = part_1(spring_list, number_list)
    memo.clear()
    result_part_2 = part_2(spring_list_copy, number_list)
    print(f"Number of possible spring combinations: {result_part_1}")
    print(f"Number of possible unfolded spring combinations: {result_part_2}")

if __name__ == "__main__":
    main()

    