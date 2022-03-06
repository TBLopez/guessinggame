#!/usr/bin/python3

import random

value = random.randint(0,10)

guess = int(input("Guess a number between 1 - 10: "))

tries = 1
    
while guess != value:
    if tries == 3:
        print("You've lost the game")
        break
    print("Try again")
    if guess > value:
        print("a little too high\n")
    if guess < value:
        print("a little too low\n")
    guess = int(input("Guess a number between 1 - 10: "))
    tries+=1
    if guess == value:
        print("You guessed correctly!")
    
