# coding=gbk
####code 1#####
from builtins import int
a = int(input("please enter a number"))
b = int(input("please enter a number"))
if a > b:
    print(a)
else:
    print(b)


####code 2####    
c = 12345

if c > 0 :
    if  len(str(c)) <= 5:
        print(len(str(c)))
    else:
        print("input nmuber is larger that 5 digits")

else:
    print("input number is wrong")
    

####code 3####

####input_number = int(input("the number you want to put in"))####

###Demo Example####
val = input('>>>')
val = int(val)
if val >= 1000:
    if val >=10000:
        print(5)
    else:
        print(4)
else:
    if val >= 100:
        if val>=10:
            print(2)
        else:
            print(1)        


###打印一个不超过的5位数#####
num = input("number is")
num_length = len(num)
num = int(num)
for i in range(num_length):
    print(num%10)
    num=num//10
    
###另外一种更好的实现方式####

my_num=input("enter a number")
my_num_length=len(my_num)
my_num=int(my_num)

for i in range(my_num_length):  #54321
    c=my_num//(10**(my_num_length-i-1))
    print(c)
    my_num= 10**(my_num_length-i-1)*c


