# Module 6 - Problem Set No. 9 - Problem 1
# YOUR NAME

import string
from random import *


def generatePassword(passwordLength):
    # string contained all of the possible characters
    possiblePasswordChars = string.ascii_letters + string.digits + '*/?-&'

    password = ''
    for i in range(passwordLength):
        randomNumber = randrange(0, len(possiblePasswordChars) - 1)
        # get a single character from the string using hte randomNumber generated

        # use accumulator pattern to create new password

    # send the password back to the caller
    return password


def main():

    # open the file to store passwords in for append
    passwordFile = open('passwords.txt', 'a')
    # how many password to generate
    numPasswords = int(input('Number of passwords would you like to generate: '))
    # desired length of password
    pwLength = int(input('Desired password length: '))

    # Write code to ensure pwLength is between 8 and 42 inclusively
    # your code here
    # if password is between 8 and 42 then call the generatePassword() function
    if pwLength >= 8 and pwLength <= 42:
        for i in range(numPasswords):
            generatedPassword = generatePassword(pwLength)

            # write password to a file
            passwordFile.write(generatedPassword + '\n')

        # close the file
        passwordFile.close()


main()
