'''
Exercise 30: Units of Pressure
(20 Lines)
In this exercise you will create a program that reads a pressure from the user in kilo-
pascals. Once the pressure has been read your program should report the equivalent
pressure in pounds per square inch, millimeters of mercury and atmospheres. Use
your research skills to determine the conversion factors between these units.
'''

print("Solution to exxercise number 30")
try:
    pressure_in_kilo_pascals : float = float(input("Enter the value of the pressure in kPa : "))
    pressure_in_pound_square_inch : float = pressure_in_kilo_pascals * 0.145038
    pressure_in_milimeters_mercury : float = pressure_in_kilo_pascals / 0.133322
    pressure_in_atm : float = pressure_in_kilo_pascals / 101.325
    print(f"The value of {pressure_in_kilo_pascals} in  pounds per square inch is : {pressure_in_pound_square_inch:.4f}")
    print(f"The value of {pressure_in_kilo_pascals} in  milimeters of mercury is : {pressure_in_milimeters_mercury:.4f}")
    print(f"The value of {pressure_in_kilo_pascals} in  atms is : {pressure_in_atm:.4f}")
except ValueError:
    print("Value Error")
except TypeError:
    print("Type Error")
