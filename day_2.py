import os
import re

full_path = os.path.join(os.getcwd(), 'Input/Day2_Input.txt')
file = open(full_path, 'r')
data = file.read()
data_list = re.split(r"[\n]+", data)

def check_report(int_report):
    diffs = [x - y for x, y in zip(int_report[1:], int_report[:-1])]
    if all([x < 0 for x in diffs]) or all([x > 0 for x in diffs]):
        if all([abs(x) >= 1 for x in diffs]) and all([abs(x) <= 3 for x in diffs]):
            return True

# Part 1
safe = 0
for report in data_list:
    int_report = [int(s) for s in report.split(' ')]
    if check_report(int_report):
        safe += 1
print(safe)

# Part 2
safe = 0
for report in data_list:
    int_report = [int(s) for s in report.split(' ')]
    sub_safe = 0
    for i in range(len(int_report)):
        if check_report(int_report[:i] + int_report[i + 1:]):
            sub_safe += 1
    if sub_safe > 0 or check_report(int_report):
        safe += 1
print(safe)




