#coding=GBK
#��ӡÿһλ���� ��ͳ�����ֳ��ֵĴ���

n = "13211445"
result = n[::-1]
print(result)
#for i in (reversed(n)):
#   print(i)


for i in range(len(n),0,-1):
    print(n[i-1],end="")




'''
dic = {}
for i in range(len(n)):
    print(n[i])
    if n[i] not in dic:
        dic[n[i]] = 1
    else:
        dic[n[i]] += 1
print(dic)
'''