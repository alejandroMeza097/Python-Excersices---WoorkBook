'''
Exercise 18: Volume of a Cylinder
(15 Lines)
The volume of a cylinder can be computed by multiplying the area of its circular
base by its height. Write a program that reads the radius of the cylinder, along with
its height, from the user and computes its volume. Display the result rounded to one
decimal place.
'''
from math import pi , pow

print("Solution to exercise number 18")
try:
    radius : float = float(input('Enter the value of the radius [M] : '))
    if radius < 0:
        raise ValueError("Radius can not be less than  zero")
    
    height : float = float(input('Enter the value of the height [M] : '))
    if height < 0:
        raise ValueError("Height can not be less than  zero")
except ValueError as ex:
    print(f"[ERROR] : {ex}")
    exit(1)

volume_of_cylinder : float = pi * pow(radius,2) * height

print(f"The value of the volume of the cylinder is : {volume_of_cylinder:.2f}")