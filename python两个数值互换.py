import dis
def func(a,b):
    a,b = b,a 
    print(a,b)

a = 10
b = 20
func(a, b)
dis.dis(func)