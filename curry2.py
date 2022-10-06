def convert(a,b):
    return a*b

def curry(func,num):
    return lambda y: func(num,y)

dollar_to_sterling = curry(convert,0.77)
print(dollar_to_sterling(5)) 