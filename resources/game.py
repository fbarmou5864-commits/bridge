#Creat a gussing game where the user has 
#to guss a secrt number between 1 and 20 
#the program should give hints if the guess
#is too high or to low, and congratulate
#the user when they guess correctly
#we need (secret_number, the player guess, while guess != secret)
import random
secret_number = random.randint(50,100)
guess = 0
while guess != secret_number: 
    guess = int(input("Guess a number between 50 and 100 !\n"))
    if guess > secret_number:
        print ("Too high, try againg!\n")
    elif guess < secret_number:
        print ("Too low, try again!\n")
    elif guess == secret_number:
        print ("Great!, you got it, the number is", secret_number)
