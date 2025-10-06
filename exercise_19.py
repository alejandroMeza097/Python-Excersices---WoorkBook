'''
Exercise 19: Free Fall
(Solved—16 Lines)
Create a program that determines how quickly an object is traveling when it hits the
ground. The user will enter the height from which the object is dropped in meters (m).
Because the object is dropped its initial speed is 0 m/s. Assume that the acceleration
due to gravity is 9.8 m/s2 . You can use the formula 
vf = √v2i + 2ad to compute the
final speed, vf , when the initial speed, vi , acceleration, a, and distance, d, are known.
'''
from math import sqrt,pow
print("Solution to exercise number 19")
height_in_meters : float = float(input("Enter the height in meters from which the object is dropped : "))
ACELERATION_GRAVITY = 9.81 # m/s^2
INICIAL_VELOCITY = 0 # m/s
final_velocity = sqrt(pow(INICIAL_VELOCITY,2) + 2 * ACELERATION_GRAVITY * height_in_meters)
print(f'The velocity of the object when hits the ground is : {final_velocity:.2f} [m/s]')