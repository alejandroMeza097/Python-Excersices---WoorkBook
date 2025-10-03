'''
Exercise 17: Heat Capacity
(Solved—25 Lines)
The amount of energy required to increase the temperature of one gram of a material
by one degree Celsius is the material’s specific heat capacity, C. The total amount
of energy required to raise m grams of a material by ΔT degrees Celsius can be
computed using the formula:
q = mCΔT.
Write a program that reads the mass of some water and the temperature change
from the user. Your program should display the total amount of energy that must be
added or removed to achieve the desired temperature change.

Extend your program so that it also computes the cost of heating the water. Elec-
tricity is normally billed using units of kilowatt hours rather than Joules. In this
exercise, you should assume that electricity costs 8.9 cents per kilowatt-hour. Use
your program to compute the cost of boiling water for a cup of coffee.
'''

print("Exercise Number 17")
try:
     mass_of_water : float = float(input("Enter the value of the mass of water [g] : "))
     if(mass_of_water < 0):
          raise ValueError("Mass must be greater than zero.")
     initial_temperature : float = float(input("Enter the value of the inicial temperature [°C] :"))
     final_temperature : float = float(input("Enter the value of the final temperature [°C] :"))
except ValueError as e :
     print(f"[ERROR] : {e}")
     exit(1) 


SPECIFIC_HEAT_OF_WATER : float = 4.186 #J/g°C
FACTOR_OF_CONVERSION : float = 1 / (3.6 * pow(10,6)) # kWh/J
COST_OF_ENERGY : float = 8.9 #cent/kWh

def calculate_cost_of_energy(energy_in_joules : float)-> float:
     return (energy_in_joules * FACTOR_OF_CONVERSION) * COST_OF_ENERGY

sensible_heat : float = mass_of_water * SPECIFIC_HEAT_OF_WATER * (final_temperature - initial_temperature)

if sensible_heat > 0 :
     print(f"You need to add : {sensible_heat:.2f} [J] to achive that temperature.")
else:
     print(f"You need to remove : {abs(sensible_heat):.2f} [J] of Joules to achive that temperature.")
     sensible_heat = abs(sensible_heat)
print(f"The amount of money to achieve that temperature is :  {calculate_cost_of_energy(sensible_heat):.5f} cents.")





     




