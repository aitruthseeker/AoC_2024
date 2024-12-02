import os
import re

full_path = os.path.join(os.getcwd(),'Input/Day1_Input.txt')
file = open(full_path,'r')
data = file.read()

data_list = re.split(r"[ \n]+", data)
data_list = [int(s) for s in data_list]
list1 = data_list[::2]
list2 = data_list[1::2]


# Part 1
list1.sort()
list2.sort()
print(sum([abs(x-y) for x,y in zip(list1, list2)]))

# Part 2
print(sum([x * list2.count(x) for x in list1]))