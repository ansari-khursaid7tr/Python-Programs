num = int(input("Enter a number: "))
if num>1:
    for i in range(2,num,1):
        if(num % i == 0):
            print(num,"is not Prime Number")
            break
        
    else:
        print(num,"is Prime Number")
    