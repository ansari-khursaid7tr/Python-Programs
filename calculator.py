from os import system
 
def input1():
    print()
    num1= int(input("Enter first number: "))
    num2= int(input("Enter second number: "))
    return num1,num2

def choice():
    choice_in = int(input("Enter your choice: "))
    check(choice_in)

def check(n):
    if(n==1):
        num1,num2 = input1()
        add(num1,num2)
    elif(n==2):
        num1,num2 = input1()
        subtract(num1,num2)
    elif(n==3):
        num1,num2 = input1()
        multiply(num1,num2)
    elif(n==4):
        num1,num2 = input1()
        divide(num1,num2)
    elif(n==5):
        exit
    else:
        print("Invalid Input")

def add(num1,num2):

    print("-"*10,"Welcome to Addition","-"*10)
    print("Sum = ",num1+num2)
    #again()

def subtract(num1,num2):
        print("-"*10,"Welcome to Subtraction","-"*10)
        print("Difference=",num1-num2)
        #again()

def multiply(num1,num2):
        print("-"*10,"Welcome to Multiplication","-"*10)
        print("Multiplication=",num1*num2)
        #again()

def divide(num1,num2):
        print("-"*10,"Welcome to Division","-"*10)
        print("Division=",num1/num2)

def main_all():
    print("Simple Calculator App")
    print("-"*50)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print("-"*50)
    choice()

def again():
    resume = input("Do you want to continue? (y/n): ")
    if(resume == 'y'):
        system('cls')
        main_all()
        again()
    else:
        print("BYE")

main_all()
again()