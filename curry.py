def multiply(a,b):
    return a*b

def mult(func,num):
    return lambda y:func(num,y)

double = mult(multiply,2)
triple = mult(multiply,3)
print(double(5))
print(triple(5))