'''
Exercise 5: Bottle Deposits
(Solved—15 Lines)
In many jurisdictions a small deposit is added to drink containers to encourage people
to recycle them. In one particular jurisdiction, drink containers holding one liter or
less have a $0.10 deposit, and drink containers holding more than one liter have a
$0.25 deposit.
Write a program that reads the number of containers of each size from the user.
Your program should continue by computing and displaying the refund that will be
received for returning those containers. Format the output so that it includes a dollar
sign and always displays exactly two decimal places.
'''


print("Excercise 5")
number_container_more_than_liter :int =int( input("Enter the number of containers that holds 1 liter or more : "))
number_container_more_less_liter : int = int (input("Enter the number of containers that holds 1 liter or less : "))
amount_deposit_more_than_liter : float = 0.10
amount_deposit_more_less_liter : float = 0.25
amount_money_containers_more_than_liter : float = amount_deposit_more_than_liter * number_container_more_than_liter
amount_money_containers_less_than_liter : float = amount_deposit_more_less_liter * number_container_more_less_liter
total_money = amount_money_containers_more_than_liter + amount_money_containers_less_than_liter
print(f"Amount earned by containers with a capacity of less than one liter : $ {amount_money_containers_less_than_liter:.2f}")
print(f"Amount earned by containers with a capacity of more than one liter :  $ {amount_money_containers_more_than_liter:.2f}")
print(f"Amount of money earned by two types of containers : $ {total_money:.2f}")
