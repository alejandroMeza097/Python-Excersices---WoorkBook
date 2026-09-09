'''
Exercise 7: Sum of the First n Positive Integers
(Solved—12 Lines)
Write a program that reads a positive integer, n, from the user and then displays the
sum of all of the integers from 1 to n. The sum of the first n positive integers can be
computed using the formula:
sum = (n)(n + 1)/2
'''

print('Exercise 7')
def sum_of_integers(number:int)->int:
    return (number * (number + 1))//2
try:
    input_number : int = int(input("Enter an integer number : "))
    if(input_number <= 0):
        raise ValueError
    print(f'The sum of the first {input_number} numbers is :{sum_of_integers(input_number)}')
except ValueError:
    print("Invalid input")
except Exception as ex:
    print("Unexpected error : ",ex)
