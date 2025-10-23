'''
Exercise 20: Ideal Gas Law
(19 Lines)
The ideal gas law is a mathematical approximation of the behavior of gasses as
pressure, volume and temperature change. It is usually stated as:
PV = nRT
where P is the pressure in Pascals, V is the volume in liters, n is the amount of
substance in moles, R is the ideal gas constant, equal to 8.314 J
mol K , and T is the
temperature in degrees Kelvin.
Write a program that computes the amount of gas in moles when the user supplies
the pressure, volume and temperature. Test your program by determining the number
of moles of gas in a SCUBA tank. A typical SCUBA tank holds 12 liters of gas at
a pressure of 20,000,000 Pascals (approximately 3,000 PSI). Room temperature is
approximately 20 degrees Celsius or 68 degrees Fahrenheit.
'''
print("Solution to exercise number 20")
try:
    pressure_in_pascals : float = float(input("Enter the value of the pressure [Pa] : "))
    volume_in_liters : float = float(input("Enter the value of the volume [L] :"))
    temperature_in_kelvin : float = float(input("Enter the value of the temperature [K] : "))
    volume_in_m3 : float = 0.001 * volume_in_liters
    CONSTANT_R : float = 8.314
    n_moles = (pressure_in_pascals * volume_in_m3 )/(CONSTANT_R * temperature_in_kelvin) 
    print(f"The quantity of moles in {volume_in_liters} liters is : {n_moles:.2f}")
except:
    print("Errors when capturing data")



