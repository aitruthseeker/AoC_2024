import os
import re

full_path = os.path.join(os.getcwd(),'Input/Day3_Input.txt')
file = open(full_path,'r')
data = file.read()

# Part 1
pairs = re.findall(r"mul\(\b([0-9]+)\b,\b([0-9]+)\b\)", data)
result = 0
for pair in pairs:
    result += int(pair[0]) * int(pair[1])
print(result)

# Part 2 - not perfect because assumes that there is no do() after last don't()
full_list = (re.findall(r"^(.*?)don't\(\)",data) + re.findall(r"do\(\)(?:(?!don't\(\)).)*", data, re.DOTALL))
new_data = ''.join( full_list)
pairs = re.findall(r"mul\(\b([0-9]+)\b,\b([0-9]+)\b\)", new_data)
result = 0
for pair in pairs:
    result += int(pair[0]) * int(pair[1])
print(result)
