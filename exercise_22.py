'''
Exercise 22: Area of a Triangle (Again)
(16 Lines)
In the previous exercise you created a program that computed the area of a triangle
when the length of its base and its height were known. It is also possible to compute
the area of a triangle when the lengths of all three sides are known. Let s1 , s2 and s3
be the lengths of the sides. Let s = (s1 + s2 + s3)/2. Then the area of the triangle
can be calculated using the following formula:
area = √s × (s − s1) × (s − s2) × (s − s3)
Develop a program that reads the lengths of the sides of a triangle from the user and
displays its area.
'''
from math import sqrt
print("Solution to exercise number 22")
try:
    side_of_triangle_1 : float = float(input("Enter the length of the first side of the triangle : [u]"))
    side_of_triangle_2 : float = float(input("Enter the length of the second side of the triangle : [u]"))
    side_of_triangle_3 : float = float(input("Enter the value of the third side of the triangle : [u]"))
    if(side_of_triangle_1 < 0 or side_of_triangle_2 < 0 or side_of_triangle_3 < 0):
        raise ValueError
    s : float = (side_of_triangle_1 + side_of_triangle_2 + side_of_triangle_3)/2
    area_of_triangle : float = sqrt(s * (s - side_of_triangle_1 )* ( s - side_of_triangle_2) * (s- side_of_triangle_3))
    print(f"The area of the triangle is : {area_of_triangle:.2f}")
except ValueError:
    print("Value error just ocurred")
