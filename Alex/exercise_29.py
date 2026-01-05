'''
Exercise 29: Celsius to Fahrenheit and Kelvin
(17 Lines)
Write a program that begins by reading a temperature from the user in degrees
Celsius. Then your program should display the equivalent temperature in degrees
Fahrenheit and degrees Kelvin. The calculations needed to convert between different
units of temperature can be found on the internet.
'''
print("Solution to exercise number 29")
try:
    degrees_celsius : float = float(input("Enter the amount of degrees celsius : "))
    celsius_to_fahrenheit : float = (9/5) * degrees_celsius + 32
    celsius_to_kelvin : float = degrees_celsius + 273.15
    print(f"{degrees_celsius} celsius is the same as {celsius_to_fahrenheit:.2f} fahrenheit")
    print(f"{degrees_celsius} celsius is the same as {celsius_to_kelvin:.2f} kelvin")

except ValueError:
    print("No valid input")

except Exception as e:
    print("An error ocurred" + e)