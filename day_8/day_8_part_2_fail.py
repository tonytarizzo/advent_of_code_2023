import re

lines = open("day_8/day_8_data.txt").read().splitlines()
location_dict = {}
directions = list(lines[0])
steps = 0

for i in lines[2:]:
    a = re.split(r"[\W]+", i)
    location_dict[a[0]] = (a[1], a[2])

curr_pos = [key for key, value in location_dict.items() if key[2] == 'A']

while (True):
    for u in directions:
        steps += 1
        for index, loc in enumerate(curr_pos):
            dict_row = location_dict.get(loc)
            if u == "L":
                curr_pos[index] = dict_row[0]
            else:
                curr_pos[index] = dict_row[1]

        if all(curr_pos[loc][2] == 'Z' for loc in range(len(curr_pos))):
            break
    else:
        continue
    break

print("output: ", steps, "steps")
