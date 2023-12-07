from functools import cmp_to_key
from scoring_functions import scoring_functions, score_5_hand

def parse_input(input_lines):
    hands = []
    for line in input_lines:
        hand, bid = line.strip().split(" ")
        hands.append((hand, int(bid)))
    return hands

def score_hand(hand, memo):
    score = memo.get(hand)
    if not score:
        score = score_5_hand(hand)
        memo[hand] = score
    return score

def score_hand_with_jokers(hand, memo):
    score = memo.get(hand)
    if not score:
        j_num = hand.count("J")
        hand_without_j = "".join([character for character in hand if character != "J"])
        score = scoring_functions[j_num](hand_without_j)
        memo[hand] = score
    return score

def solve_ties(hand_1, hand_2, tie_map):
    for char_1, char_2 in zip(hand_1, hand_2):
        if char_1 == char_2: continue
        if tie_map[char_1] > tie_map[char_2]: return 1
        return -1
    
def compare(hand_1, hand_2, scoring_function, tie_map, memo):
    hand_1_score = scoring_function(hand_1, memo)
    hand_2_score = scoring_function(hand_2, memo)
    if hand_1_score > hand_2_score: return 1
    elif hand_1_score < hand_2_score: return -1
    else: return solve_ties(hand_1, hand_2, tie_map)

def get_product_of_scores(hands):
    total = 0
    for i, hand in enumerate(hands):
        total += (i + 1) * hand[1] 
    return total

def part_1(hands):
    memo = {}
    tie_map = {character: score for score, character in enumerate("23456789TJQKA")}
    hands.sort(key=cmp_to_key(lambda x, y: compare(x[0], y[0], score_hand, tie_map, memo)))
    return get_product_of_scores(hands)

def part_2(hands):
    memo = {}
    tie_map = {character: score for score, character in enumerate("J23456789TQKA")}
    hands.sort(key=cmp_to_key(lambda x, y: compare(x[0], y[0], score_hand_with_jokers, tie_map, memo)))
    return get_product_of_scores(hands)

def main():
    with open("input.txt", "r") as input_file:
        input_lines = input_file.readlines()
    hands = parse_input(input_lines)
    result_part_1 = part_1(hands)
    result_part_2 = part_2(hands)
    print(f"Product of scores: {result_part_1}")
    print(f"Product of scores including Jokers: {result_part_2}")

if __name__ == "__main__":
    main()
    





        

