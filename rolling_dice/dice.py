#!/usr/bin/python

import random

min = 1
max = 6
roll_again = "yes"
while roll_again == "yes" or roll_again == "y":
    print("Rolling the dices...")
    num1 = random.randint(min,max)
    num2 = random.randint(min,max)
    print("Values: {0} {1}".format(num1, num2))
    roll_again = raw_input("Roll the dice again ? ")
