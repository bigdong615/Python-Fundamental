# coding=gbk
from _datetime import datetime

matrix = [[1,2,3], [4,5,6], [7,8,9]]

print('\nMethod1')
start = datetime.now()
print(start)
for c in range(100000):
    tm = [] #目标矩阵
    for row in matrix:
        for i, item in enumerate(row):
            if len(tm) < i + 1:
                tm.append([])
            
            tm[i].append(item)
            
delta = datetime.now()- start
print('total execution time is' , delta)
print(matrix)
print(tm)


#method 2 

print('\nMehtod 2')
start = datetime.now()
print(start)
for c in range(100000):
    tm = [0] * len(matrix[0])
    for i in range(len(tm)):
        tm[i] = [0] * len(matrix)
    
    for i, row in enumerate(tm):
        for j, col in enumerate(row):
            tm[i][j] = matrix[j][i]
        
delta = datetime.now()- start
print('total execution time is' , delta)
print(matrix)
print(tm)
