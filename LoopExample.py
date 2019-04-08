# coding=gbk

for i in range(10,0,-1):
    print(i)


#打印10以内的偶数
print("==================")
for i in range(10):
    if ~ i % 2 :
        print(i)
        
        
print("==================")
for i in range(10):
    if i % 2 :
        continue
        print(i)
        
        
        
print("==================")
for x in range(10):
    if x == 5 :
        break
    print(x)
    
    
print("==================")
for x in range(10):
    if x==5:
        continue
    print(x)
    

mynumber = int(input(">>>"))

if mynumber >=1000:
    if mynumber >=10000:
        print(5)
    else:
        print(4)
            
else:
    if mynumber>=100:
        print(3)
    elif mynumber>=10:
        print(2)
    else:
        print(1)
        
        