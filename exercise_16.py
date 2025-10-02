'''
Exercise 16: Area and Volume
(15 Lines)
Write a program that begins by reading a radius, r, from the user. The program will
continue by computing and displaying the area of a circle with radius r and the
volume of a sphere with radius r. Use the pi constant in the math module in your
calculations.
'''
from math import pi,pow
print("Exercise Number 16")
radius : float = float(input("Enter the value of the radius : "))
volume_sphere : float = (4/3)*pi*pow(radius,3)
print(f"The volume of the sphere is : {volume_sphere:.2f} [cubic units]")