# coding=gbk
'''
zhishu =[2,]
for number in range(2,101):
    for temp in range(2,number):
        if number%temp==0:
            continue
        if temp==number-1:
            zhishu.append(number)
print(zhishu)
    
'''



num=[];
i=2 
for i in range(2,100):
    j=2 
    for j in range(2,i):
        if i%j==0:
            break
    else:
        num.append(i)
print(num)



