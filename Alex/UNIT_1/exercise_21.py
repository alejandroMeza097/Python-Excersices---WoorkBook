'''
Exercise 21: Area of a Triangle
(13 Lines)
The area of a triangle can be computed using the following formula, where b is the
length of the base of the triangle, and h is its height:
area = b x h / 2
Write a program that allows the user to enter values for b and h. The program
should then compute and display the area of a triangle with base length b and height h.
'''
print("Exercise Number 21")
try:
    base : float = float(input("Enter the value of the base [m] : "))
    height : float = float(input("Enter the value of the height [m] : "))
    area : float = (base * height) / 2
    print(f"The value of the area is {area:.2f}")
except ValueError:
    print("No valid input or inputs")

