#coding=GBK
sql = "select * from myTable where x = 5"
for i in sql:
    print(i)
#�ַ�����һ�����ַ�������,���Ե���,��������,�����޸�  
#python3֧������
print("############")
sql ="�й�"
for i in sql:
    print(i)
    print(type(i))

print(list(sql))


tmp = "-".join(sql)
print(tmp)



lst = list(range(5))
tmp = '~~~'.join(map(str,lst))
print(tmp)

#split ���м� ���� ����
print("a b c".split(','))
print("a,b,c".split(','))


#partitionֻ��һ��
print("a,b,c".partition(','))

s = "I am very very very sorry"
print(s.find("very"))

print(s.count('very'))
print(s.startswith('very'))
print(s.endswith('very'))

print("I am %03d" % 20)
print("{:.2f}".format(3.1415926));
print ("The sum of 1+2 is {}".format(1+2))

 
