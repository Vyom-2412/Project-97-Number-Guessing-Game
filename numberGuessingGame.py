import random
print("NUmber Guessing Game")
number=random.randint(1,10)
chances = 0
print("Guess a number between 1 and 10:")

while(chances < 5):
    guess = int(input("Enter your guess :- "))

    if(guess == number):
        print("Congratulations You Won!! :D")
        break

    elif(guess < number):
        print("Your guess was too low. (Hint : Guess a number higher than)", guess)
    
    else:
        print("Your guess was too high. (Hint : Guess a number lower than)", guess)

    chances +=1

if not(chances < 5):
    print("YOU LOSE!! The number was", number)
