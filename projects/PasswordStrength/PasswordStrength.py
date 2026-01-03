

# import nessesiary libraries
import subprocess
import os
import hashlib
import time
import sys
import itertools
import string
import cmd
def get_password(password):
    # adding while true function statement in order for the password to fit every requirment even after failing check
    while True:
    # this function checks to make sure the password fits the requirements (8 length at minimum, 1 uppercase letter, 1 lowercase letter, 1 number, 1 symbol)
    # first check to see if there are any spaces first in the function (doing a loop)
        if ' ' in password:
            print("There is a space in this password please reenter the password")
            password = str(input("Enter the password: "))
        else:
            pass
    # Next if/else loop to make sure there is at least 10 numbers/letters
        if len(password) > 16:
            print("The password does not meet the maximum length of 17, please renter the password")
            password = str(input("Enter the password: "))
        else: 
            pass
    # everything beforehand has been tested to make sure password hits certain requirments
    # create a new function to ensure there has been at least 1 number
        if not any(char.isdigit() for char in password):
            print ("The password entered does not contain any numbers please renter the password")
            password = str(input("Enter the password: "))
        else:
            pass
    # everything up to here has been tested, be wary of repeat should be due to return not being indented enough
    # create a new function to check if there is 1 symbol in the password
        """if not any(not char.isalnum()for char in password):
            print("The password needs at least 1 symbol, please reenter the password")
            password = str(input("Enter the password: "))
        else:
            pass""" #orginially was kept in to make symbols more complex to crack but requires more time and makes cracking the password harder for what the project is supposed to be (basic) could add later with more improvments
    # Everything has been tested to make sure password works up until now Potentially, make the symbols not required but allowed put within the strings
    # Create a new function to check if there is 1 uppercase letter
        if not any(char.isupper()for char in password):
            print("The password is missing an Uppercase letter, please reenter")
            password = str(input("Enter the password: "))
        else:
            pass
    # Create a new function to check if there was 1 lowercase letter
        if not any(char.islower()for char in password):
            print("The password needs a lowercase letter, please renter: ")
            password = str(input("Enter the password: "))
        else:
            pass
        return password
    # The function is now correct, takes any password provided
def password_hash(password):
    # encode the string into bytes
    encoded_password = password.encode('utf-8')
    # create a hash object
    hash_object = hashlib.sha256()
    hash_object.update(encoded_password)
    hash_password = hash_object.hexdigest()
    return hash_password
# This Function will take the hashed password alongside the wordlist (rockyou.txt) to create a johntheripper script
def dictattack(hash_password):
    
    return 0
def menu():
    while True:
        print ("Password Strength Test")
        print ("\n" + "="*40)
        print("Welcome to the PasswordStrength program")
        print("The goal of this program is to evaluate a password entered and test how long it would take for the password to be guessed by Johntheripper tool")
        print("Johntheripper is a tool used to guess passwords, either by a dictionary attack and/or a brute force attack")
        print("None of the passwords entered will be saved,just will be used to provide a score on how strong your password is")
        print("The password must be at most 16 letters/numbers at most requiring 1 uppercase letter 1 lowercase letter and 1 number,symbols are allowed but not required,please enter the password below")
        print("\n" + "="*40)
        print("1. Dictionary Password Test (1)")
        print("2. Brute Force Attack (2)")
        print("3. Exit (3)")
        print("4. Quit (4)")
        print("\n" + "="*40)
        menu_option = (str(input("Please select what option you would like to choose:")))
        if menu_option == '1':
            password = str(input("Enter the password: "))
            password = get_password(password)
            hash_password = password_hash(password)
            dattack = dictattack(hash_password)
            menu_option = (str(input("Please select what option you would like to choose")))
        elif menu_option == '2':
            password = str(input("Enter the password: "))
            password = get_password(password)
            hash_password = password_hash(password)
            # finish the menu with function for brute force attack
        elif menu_option == '3':
            password = str(input("Enter the password:"))
            password = get_password(password)
            hash_password = password_hash(password)
            """Enter the function for brute force attack"""
        elif menu_option == '4':
            print("Exiting program")
            break
        else:
            print("Please reenter choice")
    return 0


# create the main statement
if __name__ == "__main__":
    # menu function for users to have options on what test to be ran, alongside providing a exit for the program
    menu()


