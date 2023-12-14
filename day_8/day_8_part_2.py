import re
from math import lcm

lines = open("day_8/day_8_data.txt").read().splitlines()
location_dict = {}
directions = list(lines[0])

for i in lines[2:]:
    a = re.split(r"[\W]+", i)
    location_dict[a[0]] = (a[1], a[2])

valid_dict = {key: value for key, value in location_dict.items() if key[2] == 'A'}

for key, value in valid_dict.items():
    curr_pos = key
    steps = 0
    while (True):
        for u in directions:
            steps += 1
            dict_row = location_dict.get(curr_pos)
            if u == "L":
                curr_pos = dict_row[0]
            else:
                curr_pos = dict_row[1]

            if curr_pos[2] == 'Z':
                break
        
        else:
            continue
        break
    valid_dict[key] = steps

print(lcm(*valid_dict.values()))
