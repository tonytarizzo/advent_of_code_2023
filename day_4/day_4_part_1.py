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

def compare_elements(row_num, winning_df, player_df):
    winning_set = set(winning_df.iloc[row_num])
    player_set = set(player_df.iloc[row_num])
    common_elements = winning_set.intersection(player_set)
    return common_elements

score = 0
for i in range(len(winning_df)):
    matches = compare_elements(i, winning_df, player_df)
    if len(matches) != 0:
        score += 2**(len(matches)-1)

print(score)




    

# score = len(common_elements)

# print(compare_elements(0, winning_df, player_df))



