# import pandas as pd
import re

with open('day_2/day_2_data.txt', 'r') as file:
    lines = file.readlines()

def check_valid(line):
    red_total = 0
    green_total = 0
    blue_total = 0

    elements = re.split(',|;|:', line)
    game_id = int(''.join(re.findall(r'\d', elements[0])))

    for element in elements[1:]:
        numbers = re.findall(r'\d+', element)
        number = int(numbers[0])

        if "red" in element:
            if number > red_total:
                red_total = number
        if "green" in element:
            if number > green_total:
                green_total = number
        if "blue" in element:
            if number > blue_total:
                blue_total = number

    power = red_total * green_total * blue_total
    return power

answers = [check_valid(line.strip()) for line in lines]

total = sum(answers)
print(total)