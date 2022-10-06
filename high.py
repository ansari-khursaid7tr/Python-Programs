
def apply(x,function):
    result = function(x)
    return result

def mult(y):
    return y*10

print(apply(5,mult))