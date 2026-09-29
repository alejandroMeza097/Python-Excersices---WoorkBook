'''
Exercise 36:Vowel orConsonant
(Solved-16 Lines)
In this exercise you will create a program that reads a letter of the alphabet from the
user. If the user enters a, e, i, o or u then your program should display a message
indicating that the entered letter is a vowel. If the user enters y then your program
should display a message indicating that sometimes y is a vowel, and sometimes y is
a consonant. Otherwise your program should display a message indicating that the
letter is a consonant.
'''


VOWELS:list[str] = ['a','e','i','o','u']
try:
    input_letter : str = input("Enter the value of a letter (just a letter)")
    if len(input_letter) >= 2 or not input_letter.isalpha() or len(input_letter) == 0:
        raise ValueError("Too many characters, zero characters or simbol entered is not a letter")
    
    if input_letter in VOWELS:
        print("The input is a vowel")

    elif input_letter == "y":
        print("sometimes y is a vowel, and sometimes y is a consonant")
        
    else:
        print("The input is a consonant")

except ValueError as ver:
    print(f"[VALUE_ERROR] : {ver}")
