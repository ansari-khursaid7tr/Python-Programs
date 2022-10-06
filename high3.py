def make_checker(s):
    if s=='even':
        return lambda n: n%2==0
    elif s=='positive':
        return lambda n:n>=0
    elif s=='negative':
        return lambda n:n<0
    else:
        return ValueError('Unknown Request')

f1 = make_checker('even')
f2 = make_checker('positive')
f3 = make_checker('negative')
print(f1(4))
print(f2(3))
print(f3(-3))