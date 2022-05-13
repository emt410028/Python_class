def add(x):
    a = 0
    for i in range(1,x+1):
        a +=i
    return a
def 乘法(x):
    a = 1
    for i in range(1,x+1):
        a = i*a
    return a

def step_乘法(x):
    a = 1
    for i in range(0,x+1,2):
        if i != 0:
            a *= i
            print(a) 
    return a

z = step_乘法(10)




print(z)