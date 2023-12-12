import re

lines = open("day_8/day_8_data.txt").read().splitlines()
location_dict = {}
directions = list(lines[0])
curr_pos = "AAA"
steps = 0

for i in lines[2:]:
    a = re.split(r"[\W]+", i)
    location_dict[a[0]] = (a[1], a[2])

while (True):
    for u in directions:
        steps += 1
        dict_row = location_dict.get(curr_pos)
        if u == "L":
            curr_pos = dict_row[0]
        else:
            curr_pos = dict_row[1]

        if curr_pos == "ZZZ":
            break
    
    else:
        continue
    break

print(steps)



