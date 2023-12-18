hand_map = {
    "FIVE_OF_A_KIND": 7,
    "FOUR_OF_A_KIND": 6,
    "FULL_HOUSE":5,
    "THREE_OF_A_KIND": 4,
    "TWO_PAIRS": 3,
    "PAIR": 2,
    "HIGH_NUMBER": 1
}
def score_5_hand(hand):
    hand_set = set(hand)
    different_cards = len(hand_set)
    if different_cards in [1, 4, 5]:
        return hand_map[{1:"FIVE_OF_A_KIND", 4: "PAIR", 5: "HIGH_NUMBER"}[different_cards]]
    if different_cards == 2:
        first_letter_count = hand.count(hand[0])
        if first_letter_count == 1 or first_letter_count == 4:
            return hand_map["FOUR_OF_A_KIND"]
        return hand_map["FULL_HOUSE"]
    hand_set_list = list(hand_set)
    if any(count == 3 for count in map(lambda x: hand.count(x), hand_set_list)):
        return hand_map["THREE_OF_A_KIND"]
    return hand_map["TWO_PAIRS"]

def score_4_hand(hand):
    hand_set = set(hand)
    hand_set_list = list(hand_set)
    different_cards = len(hand_set)
    if different_cards in [1, 3, 4]:
        return hand_map[{1: "FIVE_OF_A_KIND", 3:"THREE_OF_A_KIND", 4: "PAIR"}[different_cards]]
    first_letter_count = hand.count(hand_set_list[0])
    second_letter_count = hand.count(hand_set_list[1])
    if first_letter_count == 3 or second_letter_count == 3:
        return hand_map["FOUR_OF_A_KIND"]
    return hand_map["FULL_HOUSE"]

def score_3_hand(hand):
    different_cards = len(set(hand))
    if different_cards == 1: return hand_map["FIVE_OF_A_KIND"]
    if different_cards == 2: return hand_map["FOUR_OF_A_KIND"]
    return hand_map["THREE_OF_A_KIND"]

def score_2_hand(hand):
    if hand[0] == hand[1]:
        return hand_map["FIVE_OF_A_KIND"]
    return hand_map["FOUR_OF_A_KIND"]

score_1_or_0 = lambda x: hand_map["FIVE_OF_A_KIND"]

scoring_functions = [score_5_hand, score_4_hand, score_3_hand, score_2_hand, score_1_or_0, score_1_or_0]