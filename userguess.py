import random

def guesscomp(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        guess = random.randint(low,high)
        feedback = input(f'Is {guess} too high (h)  Too Low (L) or correct (c)???').lower()

        if(feedback == 'l'):
            low = guess + 1
        elif(feedback == 'h'):
            high = guess - 1

    print(f"YAHHH !! Computer Guess Your Number {guess}")

guesscomp(1000)
    