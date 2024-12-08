import os
import re

full_path = os.path.join(os.getcwd(),'Input/Day7_Input.txt')
file = open(full_path,'r')
data = file.read()

# Part 1
data = data.split("\n")
sum=0
for row in data:
    res = int(row.split(' ')[0].split(':')[0])
    num = list([int(s) for s in row.split(' ')[1:]])
    list_res = list([num[0]])
    for item in num[1:]:
        mult_list_res = [item * pot_res for pot_res in list_res]
        add_list_res = [item + pot_res for pot_res in list_res]
        list_res = mult_list_res + add_list_res

    if res in list_res:
        sum += res

print(sum)

# Part 2 - slow but works
sum=0
for row in data:
    res = int(row.split(' ')[0].split(':')[0])
    num = list([int(s) for s in row.split(' ')[1:]])
    list_res = list([num[0]])
    for item in num[1:]:
        mult_list_res = [item * pot_res for pot_res in list_res]
        add_list_res = [item + pot_res for pot_res in list_res]
        concat_list_res = [int(str(pot_res)+str(item)) for pot_res in list_res]
        list_res = mult_list_res + add_list_res + concat_list_res

    if res in list_res:
        sum += res

print(sum)