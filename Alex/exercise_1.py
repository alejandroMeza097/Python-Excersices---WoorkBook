"""
Exercise 1: Mailing Address
(Solved—9 Lines)
Create a program that displays your name and complete mailing address formatted in
the manner that you would usually see it on the outside of an envelope. Your program
does not need to read any input from the user.
"""

name : str = "Alejandro Jose Meza Ramos"
email:str = "alex@gmail.com"
full_message_formatted = f" name : {name} \n email : {email}"
print( "-" * len(full_message_formatted))
print(full_message_formatted)
print( "-" * len(full_message_formatted))

