#coding=GBK
sql = "select * from myTable where x = 5"
for i in sql:
    print(i)
#字符串是一个个字符的序列,可以迭代,可以索引,不可修改  
#python3支持中文
print("############")
sql ="中国"
for i in sql:
    print(i)
    print(type(i))

print(list(sql))


tmp = "-".join(sql)
print(tmp)



lst = list(range(5))
tmp = '~~~'.join(map(str,lst))
print(tmp)

#split 能切几 刀是 几刀
print("a b c".split(','))
print("a,b,c".split(','))


#partition只切一刀
print("a,b,c".partition(','))

s = "I am very very very sorry"
print(s.find("very"))

print(s.count('very'))
print(s.startswith('very'))
print(s.endswith('very'))

print("I am %03d" % 20)
print("{:.2f}".format(3.1415926));
print ("The sum of 1+2 is {}".format(1+2))

 
