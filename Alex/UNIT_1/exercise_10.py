'''
Exercise 10: Arithmetic
Create a program that reads two integers, a and b, from the user. Your program should
compute and display:
• The sum of a and b
• The difference when b is subtracted from a
• The product of a and b
• The quotient when a is divided by b
• The remainder when a is divided by b
• The result of log10 a
• The result of a^b
'''
from math import log10, pow
print("Excersice Number 10")
number_a : int  = int(input("Enter the first integer (a): "))
number_b : int  = int(input("Enter the second integer (b): "))
try:
    print(f'The sume of a and b is : {number_a + number_b}')
    print(f'The difference when b is subtracted from a is : {number_a - number_b}')
    print(f'The product of a and b is : {number_a * number_b}')
    print(f'The quotient when a is divided by b is : {number_a / number_b}')
    print(f'The remainder when a is divided by b is : {number_a % number_b}')
    print(f'The result of log10 a is : {log10(number_a)}')
    print(f'The result of a^b is : {pow(number_a,number_b)}')
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")