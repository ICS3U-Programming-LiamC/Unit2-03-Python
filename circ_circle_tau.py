#!/usr/bin/env python3

# Created By: Liam Csiffary
# Date: May 4, 2021
# This program detemines the circumference
# of a circle using tau and users radius

import constants


# creates the function where everything takes place
def main():
    # asks for users input for radius and units
    rad = float(input("\nWhat is your radius: "))
    units = input("What are your units: ")

    # declates constant tau
    constants.TAU

    # calculates circ depending on users rad
    circ = constants.TAU * rad

    # prints results to screen
    print("\nThe circumference of your circle is {}\n\
    ".format(circ, units))

    restart = input("Would you like to calculate another circumference?(y/n) ")

    if restart == "y":
        main()

    if restart == "Y":
        main()


if __name__ == "__main__":
    main()
