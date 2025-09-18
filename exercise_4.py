'''
Exercise 4: Area of a Field
(Solved—15 Lines)
Create a program that reads the length and width of a farmer’s field from the user in
feet. Display the area of the field in acres.
Hint: There are 43,560 square feet in an acre.
'''
print("Problem Number : 4")
width_in_feet : float = float(input("Enter the value of width in feet : "))
length_in_feet : float = float(input("Enter the value of length in feet : "))
rate_of_conversion = (1/43560)
area_in_acres = width_in_feet * length_in_feet * rate_of_conversion
print(f"The area of the field in acres is {area_in_acres:.3f}")