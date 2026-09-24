'''
Exercise 35:DogYears
(22 Lines)
It is commonly said that one human year is equivalent to 7 dog years. However this
simple conversion fails to recognize that dogs reach adulthood in approximately two
years. As a result, some people believe that it is better to count each of the first two
human years as 10.5 dog years, and then count each additional human year as 4 dog
years.


Write a program that implements the conversion from human years to dog years
described in the previous paragraph. Ensure that your program works correctly for
conversions of less than two human years and for conversions of two or more human
years. Your program should display an appropriate error message if the user enters
a negative number.
'''

RATE_CONVERSION_LESS_THAN_TWO : float = 10.5
RATE_CONVERSION_MORE_THAN_TWO : int = 4

try:
    human_years : float = float(input('Enter the amount of human years : '))
    dog_years : float = 0

    if human_years <= 0:
        raise ValueError("Negative Values are not allowed")
    elif human_years <= 2:
        dog_years = RATE_CONVERSION_LESS_THAN_TWO * human_years
    else:
        dog_years = (human_years - 2) * RATE_CONVERSION_MORE_THAN_TWO + 2 * RATE_CONVERSION_LESS_THAN_TWO
    print(f"Age in human years {human_years} equals {dog_years} dog years.") 

except ValueError as ve:
    print(f"Error: Invalid input. Please enter a valid number. {ve}")

