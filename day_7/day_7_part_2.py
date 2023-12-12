import pandas as pd
from collections import Counter

card_values = {'A': 12, 'K': 11, 'Q': 10, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1, 'J': 0}
hands = []
bids = []

with open ('day_7/day_7_data.txt') as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        line = line.split(' ')
        hands.append(line[0])
        bids.append(line[1])

def calc_type(hand):
    counts = Counter(hand)
    joker_count = counts.pop('J', 0)

    if joker_count:
        if joker_count == 5:
            return 5 # Five Jokers
        most_common_card, most_common_count = counts.most_common(1)[0]
        counts[most_common_card] += joker_count
    
    frequency_of_counts = Counter(counts.values())

    if 5 in frequency_of_counts:
        return 5 # Five of a Kind
    elif 4 in frequency_of_counts:
        return 4 # Four of a Kind
    elif 3 in frequency_of_counts and 2 in frequency_of_counts:
        return 3.5 # Full House
    elif 3 in frequency_of_counts:
        return 3 # Three of a Kind
    elif 2 in frequency_of_counts:
        if frequency_of_counts[2] > 1:
            return 2.5 # Two Pairs
        else:
            return 2 # One Pair
    else:
        return 1 # No Pair

def hand_strength_calc(hand):
    base = 13
    hand_strength = 0

    for card in hand:
        value = card_values[card]
        hand_strength = hand_strength * base + value

    return hand_strength

types = [None] * (len(hands))
hand_strength_array = [None] * (len(hands))

for index, hand in enumerate(hands):
    hand_type = calc_type(hand)
    hand_strength = hand_strength_calc(hand)
    types[index] = hand_type
    hand_strength_array[index] = hand_strength

df = pd.DataFrame({'hand': hands, 'bid': bids, 'type': types, 'hand_strength': hand_strength_array})
sorted_df = df.sort_values(by=['type', 'hand_strength'], ascending=[True, True])
sorted_df = sorted_df.reset_index(drop=True)
sorted_df['rank'] = sorted_df.index + 1
sorted_df['score'] = sorted_df['rank'] * sorted_df['bid'].astype(int)
total = sum(sorted_df['score'])
print(total)