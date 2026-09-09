'''
Exercise 6: Tax and Tip
(Solved—17 Lines)
The program that you create for this exercise will begin by reading the cost of a meal
ordered at a restaurant from the user. Then your program will compute the tax and
tip for the meal. Use your local tax rate when computing the amount of tax owing.
Compute the tip as 18 percent of the meal amount (without the tax). The output from
your program should include the tax amount, the tip amount, and the grand total for
the meal including both the tax and the tip. Format the output so that all of the values
are displayed using two decimal places.
'''

print("Exercise Number 6")
cost_of_meal : float = float(input("Enter de total cost of the meal in USD : "))
TAX_RATE : float = 0.16
TIP_RATE : float = 0.10
tax_of_meal: float = TAX_RATE * cost_of_meal
tip_of_meal : float = TIP_RATE * cost_of_meal
total : float = cost_of_meal + tax_of_meal + tip_of_meal
print("-------------------------")
print(f"Subtotal :$ {cost_of_meal:.2f}")
print(f"Taxes : ${tax_of_meal:.2f}")
print(f"Tip : ${tip_of_meal:.2f}")
print(f"Total : ${total:.2f}")
print("-------------------------")

