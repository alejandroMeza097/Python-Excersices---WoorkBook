'''
Exercise 11: Fuel Efficiency
(13 Lines)
In the United States, fuel efficiency for vehicles is normally expressed in miles-per-
gallon (MPG). In Canada, fuel efficiency is normally expressed in liters-per-hundred
kilometers (L/100 km). Use your research skills to determine how to convert from
MPG to L/100 km. Then create a program that reads a value from the user in American
units and displays the equivalent fuel efficiency in Canadian units.
'''
print("Excersice Number 11")

def mpg_to_liters(miles:float)->float:
    RATE_OF_CONVERSION : float = 235.214
    return RATE_OF_CONVERSION / miles

milles_per_galon : float = float(input(f'Enter the amount of MPG :'))
print(f'The {milles_per_galon} is equal to : {mpg_to_liters(milles_per_galon):.2f} L/100km')




