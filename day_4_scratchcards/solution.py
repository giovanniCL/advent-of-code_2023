def parse_input(input_lines):
    cards = []
    for line in input_lines:
        number_line = line.split(":")[1]
        winning, got = number_line.split("|")
        winning_set = set([number for number in winning.strip().split(" ") if len(number) > 0])
        got_list = [number for number in got.strip().split(" ") if len(number) > 0]
        cards.append({
            "quantity": 1,
            "winning_set": winning_set,
            "my_numbers": got_list
        })
    return cards

def part_1(cards):
    total = 0
    for card in cards:
        count = -1
        for number in card["my_numbers"]:
            if number in card["winning_set"]: count += 1
        total += 0 if count == -1 else 2 ** count
    return total

def part_2(cards):
    count = len(cards)
    for card_num, card in enumerate(cards):
        for i in range(card["quantity"]):
            offset = 1
            for number in card["my_numbers"]:
                if number in card["winning_set"]:
                    if card_num + offset < len(cards):
                        count += 1
                        cards[card_num + offset]["quantity"] += 1
                        offset += 1
    return count

def main():
    with open("input.txt", "r") as input_file:
        input_lines = input_file.readlines()
    cards = parse_input(input_lines)
    result_part_1 = part_1(cards)
    result_part_2 = part_2(cards)
    print(f"Total points: {result_part_1}")
    print(f"Total cards: {result_part_2}")

if __name__ == "__main__":
    main()