import random

min = 1
max = 6

roll_again = 'y'
while roll_again== 'y':
    print('Rolling the dice and the value is ')
    dice = random.randint(min,max)
    print(dice)
    roll_again = input("Roll the dice again? (y/n): ")