import random
import math
print ("Welcome to Sam's Math Test")
num1= random.randint(1, 10)
num2= random.randint(1, 10)
num3= random.randint(1, 10)
list=[num1, num2, num3]
maxNum= max(list)
minNum= min(list)
sqrtOne = math.sqrt(num1)

correct = False
while(correct == False):
    guess1 = int(input("Which number is the highest? "+ str(list) + ": "))
    if (maxNum == guess1):
        print("Correct!")
        correct = True
    else:
        print("Incorrect, try again")
        print(maxNum)

correct= False
while(correct == False):
    guess2= int(input("Which number is the lowest? " + str(list) +": "))
    if minNum == guess2:
     print("Correct!")
     correct = True
    else:
        print("Incorrect, try again")

correct= False
while(correct == False):
    guess3= input("Is the square root of " + str(num1) + " greater than or equal to 2? (y/n): ")
    if (sqrtOne >= 2.0 and str(guess3) == "yes"):
        print("Correct!")
        correct = True
    elif (sqrtOne < 2.0 and str(guess3) == "no"):
        print("Correct!")
        correct = True
    else:
        print("Incorrect, try again")

print("Thanks for playing!")
