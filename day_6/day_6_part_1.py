import re
import numpy as np

with open ('day_6/day_6_data.txt') as file:
    data = file.read().split('\n')
    times = re.findall(r'\d+', data[0])
    distances = re.findall(r'\d+', data[1])

def calc_distance(hold_time, time):
    return (time - hold_time)*hold_time

def find_num_variations(time, distance):
    num_variations = 0
    for i in range(time):
        trial = calc_distance(i, time)
        if trial > distance:
            num_variations += 1
    return num_variations

margins = []

for time, distance in zip(times, distances):
    time = int(time)
    distance = int(distance)
    variations = find_num_variations(time, distance)
    margins.append(variations)

margins = np.array(margins)
moe = np.prod(margins)
print(moe)
    
