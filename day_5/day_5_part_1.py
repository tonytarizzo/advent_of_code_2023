import pandas as pd
import re

with open('day_5/day_5_data.txt', 'r') as file:
    raw_lines = file.readlines()
    
seed_nums = re.findall(r'\d+', raw_lines[0])
data = ''.join(raw_lines)

def parse_text_to_df(text):
    sections = [section.strip() for section in text.strip().split('\n\n')]
    data_dict = {}

    for section in sections:
        lines = section.split('\n')
        header = lines[0].rstrip(':')
        data = [[int(num) for num in line.split()] for line in lines[1:]]
        data_dict[header] = data

    df = pd.DataFrame.from_dict(data_dict, orient='index').transpose()
    return df

class jobs:
    def __init__(self, number):
        self.number = number
    
    def find_relevant_row_index(column, number):
        possible_numbers = [item[1] for item in column if item is not None and item[1] <= number]

        if possible_numbers:
            valid_number = max(possible_numbers)
            valid_index = next(index for index, item in enumerate(column) if item is not None and item[1] == valid_number)
            if column.iloc[valid_index][1] + column.iloc[valid_index][2] >= number:
                return valid_index
            else:
                return None
        else:
            return None
    
    def get_destination_range_start(column, index, seed):
        if index == None:
            return seed
        else:
            return seed + column.iloc[index][0] - column.iloc[index][1]
    
    def process_columns(df, seed_nums):
        final_values = []
        for seed in seed_nums:
            seed = int(seed)
            # print("Seed: ", seed)
            current_value = seed

            for column_index in range(df.shape[1]):
                seed_index = jobs.find_relevant_row_index(df.iloc[:, column_index], current_value)
                # print(f"Index {column_index}: ", seed_index)
                current_value = jobs.get_destination_range_start(df.iloc[:, column_index], seed_index, current_value)
                # print(f"Destination {column_index}: ", current_value)
            # print("Final: ", current_value)
            final_values.append(current_value)
        return final_values

df = parse_text_to_df(data) 
df = df.drop(df.columns[0], axis=1) 
final_value = min(jobs.process_columns(df, seed_nums))
print(final_value)

    
    

