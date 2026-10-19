'''
Exercise 40:Name that Triangle
(Solved—20 Lines)
A triangle can be classified based on the lengths of its sides as equilateral, isosceles
or scalene. All 3 sides of an equilateral triangle have the same length. An isosceles
triangle has two sides that are the same length, and a third side that is a different
length. If all of the sides have different lengths then the triangle is scalene.
Write a program that reads the lengths of 3 sides of a triangle from the user.
Display a message indicating the type of the triangle.
'''

try:
    #user input
    side_a : float  = float(input("Enter the valur of side A : "))
    side_b : float  = float(input("Enter the valur of side B : "))
    side_c : float  = float(input("Enter the valur of side C : "))

    if side_a <= 0 or side_b <= 0 or side_c <= 0 :
        raise ValueError("The sides of the triangle must be more than zero!")
    
    if side_a == side_b and side_b == side_c:
        print("The triangle is : Equilateral")
    elif side_a == side_b or side_a == side_c or side_b == side_c:
        print("The triangle is : Isosceles")
    else:
        print("The triangle is : Scalene")

except ValueError as vaerr:
    print(f"[ERROR]: {vaerr}")




