import random

try_again = 'y'
number_of_try = 0
while try_again == 'y':
    num = random.randint(1,10)
    guess = int(input("Guess a number from 1 to 10: "))
    if(num != guess):
        print("Sorry Wrong number the number generated was ",num)
        number_of_try +=1
        print("Remaining trials = ",5-number_of_try)
        if(number_of_try == 5):
            break
        try_again = input("Do you want to continue? (y/n) :")
    else:
        print("You won")
        print("You took",number_of_try,"to guess the number")
        
if(try_again != 'y'): print("Game Over")
    