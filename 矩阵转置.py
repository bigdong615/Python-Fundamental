'''
1 2 3     1 4 7
4 5 6  ==>2 5 8
7 8 9     3 6 9
'''
from array import array



matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
count = 0
for i, row in enumerate(matrix):
    for j, col in enumerate(row):
        if i < j :
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
            count += 1
print(matrix)
print(count)

##·½·¨2###

matrix = [[1,2,3],[4,5,6],[7,8,9]]
length = len(matrix)
count = 0 
for i in range(length):
    for j in range(i): #j<i
        array[i][j],array[j][i] = array[j][i],array[i][j]
        count += 1     
print(matrix)
print(count)        
       
