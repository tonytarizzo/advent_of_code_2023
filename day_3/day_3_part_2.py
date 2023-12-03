import pandas as pd

with open('day_3/day_3_data.txt', 'r') as file:
    size = 140
    lines = file.read()
    lines_list = lines.split('\n') 
    char_lists = pd.DataFrame(list(line) for line in lines_list)

    records = []
    for y, row in char_lists.iterrows():
        for x, char in enumerate(row):
            records.append({'Character': char, 'X': x, 'Y': y})

    df = pd.DataFrame(records)

def is_specific_type(char):
    return char == "*"

def group_adjacent(digit, df, index):
    digit_list = [(digit, index)]
    forward = 0
    backward = 0
    current_index = index
    while True:
        if 0 <= current_index + 1 < len(df) and (current_index + 1) % size != 0 and df.at[current_index + 1, 'Character'].isdigit():
            digit_list.append((df.at[current_index + 1, 'Character'], current_index + 1))
            current_index += 1
            forward += 1
        else:
            break
    current_index = index
    while True:
        if 0 <= current_index - 1 < len(df) and current_index % size != 0 and df.at[current_index - 1, 'Character'].isdigit():
            digit_list.append((df.at[current_index - 1, 'Character'], current_index - 1))
            current_index -= 1
            backward -= 1
        else:
            break
    digit_list.sort(key=lambda x: x[1])
    complete_digit = int(''.join([str(item[0]) for item in digit_list]))
    return complete_digit, forward, backward

df['symbol'] = df['Character'].apply(is_specific_type)

answers_dup = []

for index in range(len(df)):
    if df.at[index, 'symbol'] == True:
        asterix_pos = index
        offsets = [-1, 1, -(size+1), -size, -(size-1), (size-1), size, (size+1)]
        for offset in offsets:
            adj_index = index + offset
            if 0 <= adj_index < len(df) and df.at[adj_index, 'Character'].isdigit():
                digit = df.at[adj_index, 'Character']
                complete_digit, forward, backward = group_adjacent(digit, df, adj_index)
                digit_start_pos = adj_index + backward
                digit_end_pos = adj_index + forward
                answers_dup.append((complete_digit, digit_start_pos, digit_end_pos, asterix_pos))

answers_dup = pd.DataFrame(answers_dup, columns=['Answer', 'Start', 'End', 'Asterix'])
answers = answers_dup.drop_duplicates()
grouped = answers.groupby('Asterix')
total_sum = 0

for _, group in grouped:
    if len(group) == 2:
        # Multiply the 'Answer' values for groups with exactly two entries
        product = group['Answer'].product()
        # Add the product to the total sum
        total_sum += product

print(total_sum)

