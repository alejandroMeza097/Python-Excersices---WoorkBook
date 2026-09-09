'''
Exercise 33: Day Old Bread
(Solved—19 Lines)
A bakery sells loaves of bread for $3.49 each. Day old bread is discounted by 60
percent. Write a program that begins by reading the number of loaves of day old
bread being purchased from the user. Then your program should display the regular
price for the bread, the discount because it is a day old, and the total price. All of the
values should be displayed using two decimal places, and the decimal points in all
of the numbers should be aligned when reasonable values are entered by the user.
'''


PRICE_BREAD_BAR : int = 3.49
PRICE_BREAD_DISCOUNT : int = 0.60
try:
    number_loaves_day_old : int = int(input('Enter the amount of loaves of day old : '))
    normal_price : int = number_loaves_day_old * PRICE_BREAD_BAR
    discount_price : int = normal_price - normal_price * PRICE_BREAD_DISCOUNT
    print(f"Number of loaves : {number_loaves_day_old}")
    print(f"Normal price : {normal_price:.2f}")
    print(f"Discount price : {discount_price:.2f}")

except ValueError as ver:
    print(f"[ERROR] {ver}")