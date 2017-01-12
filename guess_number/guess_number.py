#!/usr/bin/python

import random

min = 1
max = 100
guessed_number = random.randint(min, max)
print("Guess the number between 1 and 100...\n")
while True:
    try:
        number = raw_input("Guess a number: ")
    except:
        continue
    number = int(number)
    if number > guessed_number:
        print("{} > X, please try again".format(number))
    elif number < guessed_number:
        print("{} < X, please try again".format(number))
    else:
        print('\nNice!!! Correct number is "{}"\n'.format(number))
        play_again = raw_input("Want to play again (yes or no) : ")
        if not play_again.startswith("y"):
            break
