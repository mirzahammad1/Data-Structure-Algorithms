import numpy as np
matrix = np.array([[1,2,3,4,5],
                   [6,7,8,9,10],
                   [11,12,13,14,15],
                   [16,17,18,19,20],
                   [21,22,23,24,25]])
print('Sum of each rows')
print()
for i in range(len(matrix)):
    sum_row = 0
    for j in range(len(matrix[0])):
        sum_row += matrix[i,j]
    print(f"Sum of Row {i+1} : {sum_row}")
print()
print('Sum of each columns')
print()
for i in range(len(matrix)):
    sum_col = 0
    for j in range(len(matrix[0])):
        sum_col += matrix[j,i]
    print(f"Sum of Columns {i+1} : {sum_col}")
print()
sum_left_dig = 0
for i in range(len(matrix)):
    sum_left_dig += matrix[i,i]
print(f"Sum of left diagonal : {sum_left_dig}")
print()
sum_right_dig = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if i+j == (len(matrix)-1):
            sum_right_dig += matrix[i,j]
print(f"Sum of right diagonal : {sum_right_dig}")

