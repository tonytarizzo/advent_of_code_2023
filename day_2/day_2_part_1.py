# import pandas as pd
import re

with open('day_2/day_2_data.txt', 'r') as file:
    lines = file.readlines()

def check_valid(line):
    red_total = 12
    green_total = 13
    blue_total = 14

    elements = re.split(',|;|:', line)
    game_id = int(''.join(re.findall(r'\d', elements[0]))) 

    for element in elements[1:]:
        numbers = re.findall(r'\d+', element)
        number = int(numbers[0])

        if "red" in element and number > red_total:
            return 0
        if "green" in element and number > green_total:
            return 0
        if "blue" in element and number > blue_total:
            return 0

    return game_id

answers = [check_valid(line.strip()) for line in lines]

total = sum(answers)
print(total)