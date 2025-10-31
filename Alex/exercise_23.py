'''
Exercise 23: Area of a Regular Polygon
(Solved—14 Lines)
A polygon is regular if its sides are all the same length and the angles between all of
the adjacent sides are equal. The area of a regular polygon can be computed using
the following formula, where s is the length of a side and n is the number of sides:
area = n * s^2  / (4 * Tan(PI/n))
Write a program that reads s and n from the user and then displays the area of a
regular polygon constructed from these values.
'''
from math import tan,pi
print("Solution to exercise number 23")

try:
    length : float = float(input("Enter the value of the length : [u]"))
    sides : int = int(input("Enter the number of sides : [u]"))
    if(length < 0 or sides < 0):
        raise ValueError
    area : float = (sides * pow(length,2)) / (4 * tan(pi/sides)) 
    val = tan(pi/sides)
    print(f"The area of the polygon is : {area:.2f}")

except ValueError as verr:
    print(f"A value error just ocurred {verr}")