#!/usr/bin/env python3
# Created By: Jack Turcotte
# Date: March 18th, 2025

# Random number guessing program in python

import random


def main():

    # Create a random number
    randomNum = int(random.randrange(1, 10))
    print("For testing purposes, heres the random number: ", randomNum)

    userNumber = int(input("Enter a number between 1 and 9: "))
    correct = False

    if userNumber == randomNum:
        correct = True
        print("YOU GUESSED RIGHT!!! 🥳")

    # Check if number is higher or lower than the program number
    if userNumber > randomNum or userNumber < randomNum:
        print("Aww, not the right answer, sorry!")

    # Check if number is within the range
    if userNumber > 9 or userNumber < 1:
        print("Please enter a number within the proper range (1-9)")

    if correct == False:
        main()  # Fire main function to restart


if __name__ == "__main__":
    # Fire main function to begin
    main()
