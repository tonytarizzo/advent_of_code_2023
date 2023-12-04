import re
import pandas as pd

with open('day_4/day_4_data.txt', 'r') as file:
    lines = file.readlines()

winning_rows = []
player_rows = []

for line in lines:
    row = re.split(r'\s+', line.strip())
    if line == lines[0]:
        for i, element in enumerate(row):
            if element == '|':
                pipe_index = i
    
    winning_rows.append(row[2:pipe_index])
    player_rows.append(row[pipe_index+1:])

winning_df = pd.DataFrame(winning_rows)
player_df = pd.DataFrame(player_rows)
match_score_df = pd.DataFrame({'Copies': [1] * len(winning_df)})

def compare_elements(row_num, winning_df, player_df):
    winning_set = set(winning_df.iloc[row_num])
    player_set = set(player_df.iloc[row_num])
    common_elements = winning_set.intersection(player_set)
    return common_elements

score = 0
for i in range(len(winning_df)):
    matches = compare_elements(i, winning_df, player_df)
    match_length = len(matches)
    score_prev = score
    if match_length != 0:
        score += 2**(match_length-1)
    match_score_df.at[i, 'Matches'] = match_length
    match_score_df.at[i, 'Score'] = score - score_prev
    for extra in range(match_length):
        if i+extra+1 < len(winning_df):
            match_score_df.at[i+extra+1, 'Copies'] += 1*match_score_df.at[i, 'Copies']

total = sum(match_score_df['Copies'])
print(total)