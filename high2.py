import math

def square(num):
    return num*num

def apply(num,func):
    return func(num)

print(square(10))
print(apply(10,square))
