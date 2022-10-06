def make_function():
    def adder(x,y):
        return x+y
    return adder

f1 = make_function()
print(f1(2,3))
print(f1(6,1))
print(f1(2,12))