'''
Exercise 13: Making Change
(Solved—33 Lines)
Consider the software that runs on a self-checkout machine. One task that it must be
able to perform is to determine how much change to provide when the shopper pays
for a purchase with cash.
Write a program that begins by reading a number of cents from the user as an
integer. Then your program should compute and display the denominations of the
coins that should be used to give that amount of change to the shopper. The change
should be given using as few coins as possible. Assume that the machine is loaded
with pennies, nickels, dimes, quarters, loonies and toonies.
penny : 1 cent
Nickel : 5 cent
Dime : 10 cent
Quarter  : 25 cent
'''

PENNY : int = 1
NICKEL : int = 5
DIME : int = 10
QUARTER : int = 25
print('Exercise Number 13')
print("Enter the amount of cents : ")
try:
    inputMoney : int = int(input())
    quantity_of_quarters : int = 0
    quantity_of_dimes : int = 0
    quantity_of_nickels : int = 0
    quantity_of_pennies : int = 0
    remainder : int = 0

    if(inputMoney < 0):
        print("No negative number")
        raise Exception("Sorry, no numbers below zero")

#QUARTERS...
    if(inputMoney // QUARTER > 0):
        quantity_of_quarters = inputMoney // QUARTER
        remainder = inputMoney % QUARTER
        print(f'Quantiy of quarters : {quantity_of_quarters}') 
    else:
        quantity_of_quarters = 0
        remainder = inputMoney
        print(f'Quantiy of quarters : {quantity_of_quarters}') 

#DIMES...
    if(remainder > DIME):
        quantity_of_dimes = remainder // DIME
        remainder = remainder % DIME
        print(f'Quantiy of dimes : {quantity_of_dimes}')
    else:
        quantity_of_dimes = 0
        remainder = remainder
        print(f'Quantiy of dimes : {quantity_of_dimes}')

#NICKELS...
    if(remainder > NICKEL):
        quantity_of_nickels = remainder // NICKEL
        remainder = remainder % NICKEL
        print(f'Quantiy of nickels : {quantity_of_nickels}')
    else:
        quantity_of_nickels = 0
        remainder = remainder
        print(f'Quantiy of nickels : {quantity_of_nickels}')

#PENNIES
    if(remainder > PENNY):
        quantity_of_dimes = remainder
        print(f'Quantiy of pennies : {quantity_of_dimes}')
    else:
        remainder = remainder  
        print(f'Quantiy of pennies : {remainder}')
except :
    print("Error !")

