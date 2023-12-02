import pandas as pd
import re

total = 0

def find_digits(df):
    digit_positions = []
    total_digits = 0

    for match in re.finditer(r'\d', df):
        digit = match.group()
        digit_positions.append((digit))
    
    if digit_positions:
        first_digit = digit_positions[0]
        last_digit = digit_positions[-1]

    else:
        first_digit = 0
        last_digit = 0
    
    first_digit = int(first_digit)
    last_digit = int(last_digit)
    total_digits += first_digit * 10 + last_digit

    return total_digits

with open('day_1_data.txt', 'r') as file:
    lines = file.readlines()

answers = [find_digits(line.strip()) for line in lines]

total = sum(answers)
print(total)


