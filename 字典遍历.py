'''
x = 3 
print(eval("3+2"))
print("3+2")
'''
d ={}
d =dict.fromkeys(range(5), 100)
'''
print(d)

for key in d:
    print(d[key])
    
for key in d.keys():
    print(d.get(key))
    
for value in d.values():
    print(value)

for item in d.items():
    print(item)
'''
    
for item in d.items():
    #print(item[0],item[1])
    print(item)

#for k,v in d.items():
#    print(k,v)
    
#for k, _ in d.items():
#    print(k)
    
#for _,v in d.items():
#    print(v)
    
mylst= list(enumerate(range(5)))
print(mylst)   