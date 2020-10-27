
## Author: Feras Isied
## Problem: A program that counts up the number of 
##  vowels contained in the string
## Formula: vowels are a,e,i,o,u

def vowelChecker():
    stringInput = input("Enter a word to check if the" +
    " it has a vowel!\n").lower() # lower case string
    
    counter = 0
    for letters in stringInput:
        if (letters in ('a','e','i','o','u')):
            counter += 1
    print("Nunber of vowels:", counter)
vowelChecker()
