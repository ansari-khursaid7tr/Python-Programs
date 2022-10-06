'''a=2
b=3

a,b = b,a
print(a," ",b)'''

def swap(a,b):
    return b,a

num = 2
num2 = 3
x,y = swap (num,num2)
print(x,y)