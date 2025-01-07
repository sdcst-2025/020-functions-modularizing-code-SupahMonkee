"""
Task 2:
Create a program to play a number guessing game
There should be a function:
title()
displays instructions and how to play

game()
plays the games
"""

import random, os


def title():
    os.system('cls')
    print('Welcome to Number Guesser')
    print('=========================')
    print("Guess a number from 1-100.")
    print('You will be told if your answer is too low or too high.')
    input('Press enter when you are ready.')
    os.system('cls')

def game():
    answer = random.randrange(1,100)
    guess = 0
    attempt = 0
    win = False
    while win == False:
        if guess != 0:
            print(f'Your previous guess was {guess}.')
        guess = int(input("Enter your guess: "))
        if guess < answer:
            os.system('cls')
            print('You guessed too low.')
        if guess > answer:
            os.system('cls') 
            print('You guessed too high.')
        if guess == answer:
            os.system('cls')
            win = True
        attempt += 1
    if attempt == 1:
        print('Wow! You guessed it first try!')
        print(f'The number was {answer}.')
    elif attempt > 1:
        print(f'Nice! It took {attempt} guesses.')
        print(f'The number was {answer}.')

title()
game()

#done