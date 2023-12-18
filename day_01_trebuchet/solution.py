DIGITS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}
DIGITS_REVERSED = {key[::-1]: value for key, value in DIGITS.items()}
PARTIAL_DIGITS = set(["thr", "fou", "fiv", "sev", "eig", "nin", "thre", "seve", "eigh"])
PARTIAL_DIGITS_REVERSED = set(["eer", "ruo", "evi", "nev", "thg", "eni", "eerh", "neve", "thgi"])

def part_1(lines):
    total = 0
    for line in lines:
        left = 0
        right = -1
        char_left = line[left]
        char_right = line[right]
        while not char_left.isdigit() and not char_right.isdigit():
            left +=1
            right -= 1
            char_left = line[left]
            char_right = line[right]
        while not char_left.isdigit():
            left +=1
            char_left = line[left]
        while not char_right.isdigit():
            right -=1
            char_right = line[right]
        total += int(char_left + char_right)
    return total

def find_first_digit(line, digits=DIGITS, partial_digits=PARTIAL_DIGITS):
    start = 0
    end = 3
    line_length = len(line)
    while end < line_length:
        if line[start].isdigit(): return line[start]
        for extension in range(3):
            word = line[start:end + extension]
            if word in digits: return digits[word]
            elif word in partial_digits: continue
            else: break
        start += 1
        end += 1
    while start < line_length:
        if line[start].isdigit(): return line[start]
        start += 1

def part_2(lines):
    total = 0
    for line in lines:
        left_char = find_first_digit(line)
        right_char = find_first_digit(line[::-1], DIGITS_REVERSED, PARTIAL_DIGITS_REVERSED)
        total += int(left_char + right_char)
    return total

def main():
    with open("input.txt", 'r') as input_file:
        input_lines = input_file.readlines()
    result_part_1 = part_1(input_lines)
    result_part_2 = part_2(input_lines)
    print(f"Sum of calibration values: {result_part_1}")
    print(f"Real sum of calibration values (including digits written in english): {result_part_2}")

if __name__ == "__main__":
    main()


        



