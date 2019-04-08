a = int(input("enter a number>>>"))
b = int(input("enter a number>>>"))
c = int(input("enter a number>>>"))
'''method 1
if a > b:
    if a > c:
        if b > c:
            print(a,b,c)
        else:
            print(a,c,b)
    else:
        print(c,a,b)

else:
    if b > c:
        if a > c:
            print(b,a,c)
        else:
            print(b,c,a)
    else:
        print(c,b,a)

'''


'''method 2 
top = max(a,b,c)
 
bottom = min(a,b,c)

middle = a + b + c - top - bottom

print(top,middle,bottom)
'''
        
        
        
'''method3        
mylist=[a,b,c]
mylist.sort()
print(mylist)
'''

'''use max() method
nums = [a,b,c]
while True:
    x = max(nums)
    print(x)
    nums.remove(x)
    if len(nums) == 1:
        print(nums[0])
        break
'''
##bubble sorting algrithem
lst = [a,b,c]
length = len(lst)
for i in range(length):
    for j in range(length - 1 - i):
        if lst[j] > lst[j+1]:
            lst[j],lst[j+1]=lst[j+1],lst[j]
            #tmp = lst[j]
            #lst[j] = lst[j+1]
            #lst[j+1] = tmp
            
print(lst)            
        


    

    
    