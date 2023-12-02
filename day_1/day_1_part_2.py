import pandas as pd
import re

total = 0
firsts = 0
lasts = 0

def first_digit(df, firsts):
    replacements = {"one": "one1one", "two": "two2two", "three": "three3three","four": "four4four", "five": "five5five", "six": "six6six","seven": "seven7seven", "eight": "eight8eight", "nine": "nine9nine"}
    for old, new in replacements.items():
        df = df.replace(old, new)
    digit_positions = []

    for match in re.finditer(r'\d', df):
        digit = match.group()
        digit_positions.append((digit))
    
    if digit_positions:
        first_digit = digit_positions[0]

    else:
        first_digit = 0
    
    first_digit = int(first_digit)
    firsts += first_digit
    return firsts

def last_digit(df, lasts):
    replacements = {"one": "one1one", "two": "two2two", "three": "three3three","four": "four4four", "five": "five5five", "six": "six6six","seven": "seven7seven", "eight": "eight8eight", "nine": "nine9nine"}
    replacements = {key[::-1]: value[::-1] for key, value in replacements.items()}
    df = df[::-1]
    for old, new in replacements.items():
        df = df.replace(old, new)
    
    digit_positions = []
    for match in re.finditer(r'\d', df):
        digit = match.group()
        digit_positions.append((digit))
    
    if digit_positions:
        last_digit = digit_positions[0]

    else:
        last_digit = 0
    
    last_digit = int(last_digit)
    lasts += last_digit
    return lasts

with open('day_1/day_1_data.txt', 'r') as file:
    lines = file.readlines()

answers_first = [first_digit(line.strip(), firsts) for line in lines]
answers_last = [last_digit(line.strip(), lasts) for line in lines]

answers = [answers_first[i]*10 + answers_last[i] for i in range(len(answers_first))]
total = sum(answers)
print(total)