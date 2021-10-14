#Developer: Logann Johnson
#Date: 10.11.21
#Program: ATM Bank Transaction

"""
This program simulates an ATM utilizing If, Elis, & Else statements
Nesting If statements and refresh our Comparison & Logical Operators
"""

print("Welcome to Cash-R-Us Bank\nLet's take a moment to set up your account.\n")

# Set up account by asking users for their First & Last name using Variables

firstName = input("What is your first name: ")
lastName = input("What is your last name: ")

print("\nWelcome to Cash-R-Us", firstName,lastName + ", we will now set up a security PIN on your account. \n")

# Set up a PIN - Personal Identification Number
pin = input("Please choose a 4 digit Personal Identification Number: ")

print("\nThank you",firstName + ", we see that you set your PIN to",pin)