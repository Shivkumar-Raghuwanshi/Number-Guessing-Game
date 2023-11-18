# /////////////////////////////////////////////////////////////////#
# Method 1

from math import log2
from random import randint
# Taking inputs
lower_limit = int(input("Please enter the lower limit: "))
# Taking inputs
upper_limit = int(input("Please enter the upper limit: "))

# generating random number between the lower and upper limit
random_number = randint(lower_limit, upper_limit)
number_of_chances = round(log2(upper_limit - lower_limit + 1))
print('You have only', number_of_chances, 'chances to guess the integer!')

# Initializing the number of guesses using while loop and if-elif-else conditional statements.
count = 0
while(count<number_of_chances):
    guess = int(input('Please guess a number: '))
    count +=1
    # Condition Checking
    if random_number == guess:
        print('Congratulations you did it in ', count, "attempt")
        break
    elif random_number > guess:
        print("Your guessed number is less than the target!")
    elif random_number < guess:
        print("Your guessed number is greater than the target!")
 
 # If Guessing is more than required guesses, shows this output       
if count >= number_of_chances:
    print('The target number is :', random_number)
    print("Best of Luck for Next time!")

# ///////////////////////////////////////////////////////////////////////////////////////////#
# Method 2
# Initializing the number of guesses using function and while loop with conditional statements.
from math import log2
from random import randint

def guess_the_number():
    # Taking inputs
    lower_limit = int(input("Please enter the lower limit: "))
    upper_limit = int(input("Please enter the upper limit: "))
    
    # generating random number between the lower and upper limit
    random_number = randint(lower_limit, upper_limit)
    number_of_chances = round(log2(upper_limit - lower_limit + 1))
    print('You have only', number_of_chances, 'chances to guess the integer!')
    
    count = 0
    while(count<number_of_chances):
        guess = int(input('Please guess a number: '))
        count +=1
    # Condition Checking
        if random_number == guess:
            print('Congratulations you did it in ', count, "attempt")
            break
        elif random_number > guess:
            print("Your guessed number is less than the target!")
        elif random_number < guess:
            print("Your guessed number is greater than the target!")
     
    if count >= number_of_chances:
        print('The target number is :', random_number)
        print("Best of Luck for Next time!")
if __name__ == '__main__':
    guess_the_number()

