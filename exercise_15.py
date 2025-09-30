'''
Exercise 15: Distance Units
(20 Lines)
In this exercise, you will create a program that begins by reading a measurement
in feet from the user. Then your program should display the equivalent distance in
inches, yards and miles. Use the Internet to look up the necessary conversion factors
if you don’t have them memorized.
'''
print('Exercise Number 15')
measure_in_feet : float = float(input("Enter  your measure in feet : "))
factor_feet_to_yards : float = 1/3
factor_feet_to_inches : float = 12
factor_feet_to_miles : float = 1/5280
print(f'The equivalence of {measure_in_feet} to yards is :  {factor_feet_to_yards * measure_in_feet:.2f}')
print(f'The equivalence of {measure_in_feet} to inches is :  {factor_feet_to_inches * measure_in_feet:.2f}')
print(f'The equivalence of {measure_in_feet} to miles is :  {factor_feet_to_miles * measure_in_feet:.6f}')
