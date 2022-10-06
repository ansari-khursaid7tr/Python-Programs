P = input("\n Enter the principal amount: ")
T = input("\n Enter the time: ")
R = input("\n Enter the rate: ")

Si = (int(P) * float(T) * float(R) ) /100
Ci = int(P) * (((1 + float(R)/100) ** int(T)) - 1)
print("\n Simple Interest = ",Si)
print("\n Compound Interest = ",Ci)