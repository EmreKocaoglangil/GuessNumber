import random
def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess  a number between 1 and {x} :'))
        if guess < random_number:
            print("Sorry your guess is too low.Try Again.")
        elif guess > random_number:
            print("Sorry your guess is too high.Try Again.")    
    
    print("Gz ! You found the correct number.")

def computer_guess(x):
    lowest_number = 0
    highest_number = x
    feedback = ""
    while feedback != "C" :
        guess = random.randint(lowest_number,highest_number)
        feedback = input(f"Is my guess {guess} too low (L), too high (H) or Correct (C)")
        if feedback == "L": 
            lowest_number = guess+1
        elif feedback == "H":
            highest_number = guess-1
    print (f"Your number was {guess}. Am I correct :) ?")        
computer_guess(10)