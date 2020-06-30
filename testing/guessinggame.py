import random
highest=10
answer=random.randrange(highest)
guess=raw_input("guess a number from 0 to %d: " %highest)
while (int(guess)!=answer):
    if(int(guess)<answer):
        print('answer is higher')
    else:
        print('answer is lower')
    guess=raw_input("guess a number from 0 to %d: " %highest)
raw_input('you are a Winner face!!!')
