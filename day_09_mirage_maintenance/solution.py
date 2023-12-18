def get_next_sequence(sequence):
    new_sequence = []
    for i in range(1, len(sequence)):
        new_sequence.append(sequence[i] - sequence[i - 1])
    return new_sequence

def get_sequences(sequence):
    current = sequence
    new_sequences = [current]
    while not all([number == 0 for number in current]):
        current = get_next_sequence(current)
        new_sequences.append(current)
    return new_sequences
    
def extrapolate_future(sequences):
    new_sequences = [sequence.copy() for sequence in sequences]
    new_sequences[-1].append(0)
    for i in range(len(new_sequences) - 1, 0, -1):
        new_sequences[i - 1].append(new_sequences[i][-1] + new_sequences[i - 1][-1])
    return new_sequences

def extrapolate_past(sequences):
    new_sequences = [sequence.copy() for sequence in sequences]
    new_sequences[-1] = [0, *new_sequences[-1]]
    for i in range(len(new_sequences) - 1, 0, -1):
        new_sequences[i - 1] = [new_sequences[i - 1][0] - new_sequences[i][0], *new_sequences[i -1]]
    return new_sequences

def part_1(sequences):
    total = 0
    for sequence in sequences:
        sequence_list = get_sequences(sequence)
        new_sequence_list = extrapolate_future(sequence_list)
        total += new_sequence_list[0][-1]
    return total

def part_2(sequences):
    total = 0
    for sequence in sequences:
        sequence_list = get_sequences(sequence)
        new_sequence_list = extrapolate_past(sequence_list)
        total += new_sequence_list[0][0]
    return total

def main():
    with open("input.txt", "r") as input_file:
        input_lines = input_file.readlines()
    sequences = []
    for line in input_lines:
        sequences.append(list(map(int, line.strip().split(" "))))
    result_part_1 = part_1(sequences)
    result_part_2 = part_2(sequences)
    print(f"Sum of extrapolated values for the future: {result_part_1}")
    print(f"Sum of extrapolated values for the past: {result_part_2}")

if __name__ == "__main__":
    main()

    