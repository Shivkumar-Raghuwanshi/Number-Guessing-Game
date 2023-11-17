from math import log2
from random import randint

# Taking inputs
lowerLimit = int(input("Please enter the lower limit: "))
# Taking inputs
upperLimit = int(input("Please enter the upper limit: "))

# generating random number between the lower and upper limit
randomNumber = randint(lowerLimit, upperLimit)
minimumChances = round(log2(upperLimit - lowerLimit + 1)
)
print('You have only', minimumChances, 'chances to guess the integer!')

# Initializing the number of guesses.
count = 0
while(count<minimumChances):
    guess = int(input('Please guess a number: '))
    count +=1
    # Condition Checking
    if randomNumber == guess:
        print('Congratulations you did it in ', count, "attempt")
        break
    elif randomNumber > guess:
        print("Your guessed number is less than the target!")
    elif randomNumber < guess:
        print("Your guessed number is greater than the target!")
 
 # If Guessing is more than required guesses, shows this output       
if count >= minimumChances:
    print('The target number is :', randomNumber)
    print("Best of Luck for Next time!")
