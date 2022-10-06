var =10

def myfun():
    global var
    var +=1
    print(var)

myfun()
print(var)