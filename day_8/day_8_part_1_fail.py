import numpy as np

with open ('day_8/day_8_data.txt') as file:
    lines = file.readlines()
    directions = lines[0].strip()
    left_array = np.array([None] * (len(lines) - 2))
    right_array = np.array([None] * (len(lines) - 2))
    starting_array = np.array([None] * (len(lines) - 2))

    for i, line in enumerate(lines[2:]):
        line = line.strip()
        line = line.split(' ')
        line = [element.replace('(', '').replace(')', '').replace(',', '') for element in line]
        starting_array[i] = line[0]
        left_array[i] = line[2]
        right_array[i] = line[3]

index = 0
step_count = 0
curr_pos = starting_array[index]

while (True):
    for char in directions:
        if char == 'L':
            curr_pos = left_array[index]
        elif char == 'R':
            curr_pos = right_array[index]

        step_count += 1
        index = np.where(starting_array == curr_pos)[0]

        if curr_pos == "ZZZ":
            break
    if curr_pos == "ZZZ":
        break

print("answer", step_count)