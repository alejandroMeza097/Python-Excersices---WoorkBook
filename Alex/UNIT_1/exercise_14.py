'''
Exercise 14: Height Units
(Solved—16 Lines)
Many people think about their height in feet and inches, even in some countries that
primarily use the metric system. Write a program that reads a number of feet from
the user, followed by a number of inches. Once these values are read, your program
should compute and display the equivalent number of centimeters.
'''
print("Exercise Number 14")
height_in_feet : float = float(input("Enter the first value of your height in feet :"))
height_in_inches : float = float(input("Enter the second value of your height in inches :"))
height_feet_to_cm : float = height_in_feet * 30.48
height_inches_to_cm : float = height_in_inches * 2.54
total_height_cm = height_feet_to_cm + height_inches_to_cm
print(f'The height in cm is : {total_height_cm:.2f}')