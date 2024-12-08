import os
import re

full_path = os.path.join(os.getcwd(),'Input/Day4_Input.txt')
file = open(full_path,'r')
data = file.read()

# Part 1
data = data.split("\n")

# forward and backwards check for XMAS
def xmas_count(some_str):
    return len(re.findall('XMAS',some_str)) + len(re.findall('XMAS',some_str[::-1]))
# Rows
xmas_rows = 0
for row in data:
    xmas_rows += xmas_count(row)

# Columns
xmas_cols = 0
for col in range(len(data[0])):
    col_str = ''
    for row in data:
        col_str += row[col]
    xmas_cols += xmas_count(col_str)

# Diagonals
xmas_diag = 0
n_rows = len(data)
n_cols = len(data[0])
for i in range(len(data[0])):
    if i == 0:
        diag_right = ''.join([data[x][x] for x in range(n_rows)])
        diag_left = ''.join([data[x][n_cols-1-x] for x in range(n_rows)])
        xmas_diag += xmas_count(diag_right) + xmas_count(diag_left)
    else:
        # Upper Diagonal
        diag_str_upper_right = ''.join([(data[x][x+i]) for x in range(n_rows-i)])
        diag_str_upper_left = ''.join([(data[x][n_cols-1-x-i]) for x in range(n_rows-i)])
        diag_str_lower_right = ''.join([(data[x+i][x]) for x in range(n_rows - i)])
        diag_str_lower_left = ''.join([(data[x+i][n_cols-x-1]) for x in range(n_rows-i)])
        xmas_diag += xmas_count(diag_str_upper_right) + xmas_count(diag_str_upper_left) + xmas_count(diag_str_lower_right) + xmas_count(diag_str_lower_left)


print(xmas_cols+xmas_rows+xmas_diag)