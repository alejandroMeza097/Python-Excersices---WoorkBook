'''
Exercise 28: Wind Chill
(Solved—22 Lines)
When the wind blows in cold weather, the air feels even colder than it actually is
because the movement of the air increases the rate of cooling for warm objects, like
people. This effect is known as wind chill.
In 2001, Canada, the United Kingdom and the United States adopted the fol-
lowing formula for computing the wind chill index. Within the formula Ta is the
air temperature in degrees Celsius and V is the wind speed in kilometers per hour.
A similar formula with different constant values can be used with temperatures in
degrees Fahrenheit and wind speeds in miles per hour.

WCI = 13.12 + 0.6215Ta - 11.37V 0.16 + 0.3965Ta V 0.16

Write a program that begins by reading the air temperature and wind speed from the
user. Once these values have been read your program should display the wind chill
index rounded to the closest integer.
The wind chill index is only considered valid for temperatures less than or
equal to 10 degrees Celsius and wind speeds exceeding 4.8 kilometers per
hour.
'''

print("Solution to exercise number : 28")

def wind_chill_wind_calculation(air_temp : float,speed_wind : float):
    return 13.12 + 0.6215 * air_temp - 11.37 * (speed_wind ** 0.16) + 0.3965 * air_temp * (speed_wind ** 0.16)

try:
    air_temperatue : float = float(input("Enter the value of the aire temperature  [°C] : "))
    if(air_temperatue > 10):
        raise ValueError("air temperature out of range")
    
    wind_speed : float = float(input("Enter the value of the wind speed [km/h] : "))
    if(wind_speed > 4.8):
        raise ValueError("wind speed out of range")
    
    print(f"The wind chill index is : {round(wind_chill_wind_calculation(air_temperatue,wind_speed))}")
    
except ValueError as ve:
    print(f"An error ocurred : {ve}")

except Exception as e:
     print(f"An error ocurred : {e}")