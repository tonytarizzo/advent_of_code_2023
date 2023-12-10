import re
import numpy as np

with open ('day_6/day_6_data.txt') as file:
    data = file.read().split('\n')
    times = re.findall(r'\d+', data[0])
    time = int(''.join(times))
    distances = re.findall(r'\d+', data[1])
    distance = int(''.join(distances))

def calc_distance(hold_time, time):
    return (time - hold_time)*hold_time

def find_num_variations(time, distance):
    num_variations = 0
    for i in range(time):
        trial = calc_distance(i, time)
        if trial > distance:
            num_variations += 1
    return num_variations

variations = find_num_variations(time, distance)
print(variations)
    
