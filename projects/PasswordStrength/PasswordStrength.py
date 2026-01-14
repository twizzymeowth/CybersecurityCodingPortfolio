# importing necessary libraries
# subprocess to implement John the Ripper
# import cmd
import cmd
import subprocess
# to create MD5 hashes
import hashlib
# for file paths/linux
import os
# Validate the hashes
import re
# to get a time count for the attacks
import time
# to import string
import string
# creating function definitions
# validate_password -> to verify passwords entered making sure they fit the requirements
# (8-10 characters requiring at least 1 uppercase, 1 lowercase, 1 number)
def validate_password(password):
    # adding while true function statement in order for the password to fit every requirement even after failing check
    while True:
    # this function checks to make sure the password fits the requirements (8 length at minimum, 1 uppercase letter, 1 lowercase letter, 1 number, 1 symbol)
    # check to see if there are any empty spaces in the password
        if ' ' in password:
            print("There is a space in this password please reenter the password")
            password = str(input("Enter the password: "))
        else:
            pass
    # Minimum and maximum length requirements
        if len(password) > 10:
            print("The password does not meet the maximum length of 10, please renter the password")
            password = str(input("Enter the password: "))
        elif len(password) < 8:
            print("The password does not meet the minimum length requirement of 8, please renter the password.")
            password = str(input("Enter the password: "))
        else: 
            pass
    # Number requirement
        if not any(char.isdigit() for char in password):
            print ("The password entered does not contain any numbers please renter the password")
            password = str(input("Enter the password: "))
        else:
            pass
    # Uppercase letter requirement
        if not any(char.isupper()for char in password):
            print("The password is missing an Uppercase letter, please reenter")
            password = str(input("Enter the password: "))
        else:
            pass
    # Lowercase letter requirement
        if not any(char.islower()for char in password):
            print("The password needs a lowercase letter, please renter: ")
            password = str(input("Enter the password: "))
        else:
            pass
        return password
# Converting the entered password into sha256 bytes 
def password_hash(password):
    # Try loop to verify its done and excepts in case of any errors
    # create a hash values
    try:
        hash_sha256 = hashlib.sha256(password.encode()).hexdigest()
    except TypeError as t:
        print(f"TypeError: {t}")
    except AttributeError as a:
        print(f"AttributeError: {a}")
    except ValueError as V:
        print(f"ValueError: {V}")
    # Else statement to have it run with subprocess if correct
    else:
        # send to hashfile.txt for John the Ripper
        # Could both
        with open("hashfile.txt","w") as f:
            f.write(hash_sha256 + "\n")
            return hash_sha256
# Function for the dict attack
def JTR_dict():
    print("Starting Dictionary Attack with Rules (Enhanced)")
    # Get the directories where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    hashfile_path = os.path.join(script_dir, "hashfile.txt")
    wordlist_path = os.path.join(script_dir, "rockyou.txt")
    john_path = os.path.join(script_dir, "john", "run", "john")
    john_conf = os.path.join(script_dir, "john", "run", "john.conf")
    # Testing to check the paths work before testing
    if not os.path.exists(hashfile_path):
        print("Error: hashfile.txt not found!")
        return 0
    
    if not os.path.exists(wordlist_path):
        print("Error: rockyou.txt wordlist not found!")
        return 0
    
    if not os.path.exists(john_path):
        print("Error: John the Ripper binary not found!")
        return 0
    
    # Clear any previous session
    pot_file = os.path.join(script_dir, "john", "run", "john.pot")
    if os.path.exists(pot_file):
        os.remove(pot_file)
    
    try:
        # Using --rules=Wordlist applies common transformations:
        # - Adding numbers (0-9, 00-99)
        # - Adding symbols (!@#$%^&*)
        # - Capitalizing first letter
        # - l33t speak substitutions
        # This catches passwords like "Password9!" from base word "password"
        result = subprocess.run(
            [john_path, f"--wordlist={wordlist_path}", "--rules=Wordlist", "--format=Raw-SHA256", hashfile_path],
            capture_output=True,
            text=True,
            timeout=120
        )
    except FileNotFoundError as e:
        print(f"File was not found")
        return 0
    except subprocess.TimeoutExpired:
        print(f"Attack has timed out")
    except PermissionError:
        print(f"Permission Denied")
    else:
        print(result.stdout)
        return result
# function for JTR_Brute():
"""
def JTR_Brute():
# Function for Brute Force attack
    start_time = time.time()

    # try statement in order to start the attack,so that error doesnt crash program 
    try:
        # Using subprocess.run
        # placeholder to let base run
        print ("hi")
        # placeholder
        # dict_result = subprocess.run
    finally:
        return 0 
"""
# Menu function for each option
def menu():
    while True:
        print ("Password Strength Test")
        print ("\n" + "="*40)
        print("Welcome to the PasswordStrength program")
        print("The goal of this program is to evaluate a password entered and test how long it would take for the password to be guessed by Johntheripper tool")
        print("Johntheripper is a tool used to guess passwords, either by a dictionary attack and/or a brute force attack")
        print("None of the passwords entered will be saved,just will be used to provide a score on how strong your password is")
        print("8-10 characters requiring at least 1 uppercase, 1 lowercase, 1 number")
        print("\n" + "="*40)
        # if user would like rubric
        # validate password
        usrpassword = str(input("Enter the password below:\n"))
        usrpassword = validate_password(usrpassword)
        # convert to hash file
        hash_value  = password_hash(usrpassword)
        print("Your password will be evaluated by testing it against a software tool known as John the Ripper""\n""This tool is used to crack passwords by deploying different attacks")
        print("\n" + "="*40)
        print("1. Dictionary Attack")
        print("="*40)
        print("Dictionary Attacks are done by testing the entered password against a word list of commonly used passwords")
        print("Dictionary attacks are quicker but also not as through as brute force attacks")
        print("="*40)
        print("2. Brute Force")
        print("="*40)
        print("Brute Force Attacks are done by john the ripper running running password combinations in order to crack the password")
        print("Brute Force Attacks are more in depth and take longer, for this program it will instead be a estimate of how long it would take to crack")
        print("="*40)
        print("type EXIT to leave prompt at any time")
        # asking user for input
        JTR = str(input(f"Please enter below which attack you would like done {1} Dictionary Attack {2} Brute Force: "))
        # create function to check user input for which JTR attack they would like done
        if JTR == "1":
            JTR_dict()
        elif JTR == "2":
            print("Brute Force not yet implemented")
            # this will be for the brute force options
        elif JTR.upper() == "EXIT":
            print("Exiting program...")
            break
        else:
            print("Please Reenter option, 1 is for dictionary attack 2 for brute force")

if __name__ == "__main__":
    menu()

    
