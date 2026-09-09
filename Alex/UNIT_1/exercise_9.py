'''
Exercise 9: Compound Interest
(19 Lines)
Pretend that you have just opened a new savings account that earns 4 percent interest
per year. The interest that you earn is paid at the end of the year, and is added
to the balance of the savings account. Write a program that begins by reading the
amount of money deposited into the account from the user. Then your program should
compute and display the amount in the savings account after 1, 2, and 3 years. Display
each amount so that it is rounded to 2 decimal places.
'''
from math import pow
print("Excersice Number 9")
amount_of_money : float = float(input("Enter the amount of money :"))
percent_interest : float = 0.05
years_of_saving : int = 2

def calculate_savings(years) -> float:
    return amount_of_money * pow(percent_interest + 1 , years)

for year in range(1,years_of_saving + 1):
    print(f'Year : {year}')
    print(f'Ammout : {calculate_savings(year):.2f}')

