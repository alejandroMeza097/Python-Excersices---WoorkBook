'''Exercise 32: Sort 3 Integers
(Solved—19 Lines)
Create a program that reads three integers from the user and displays them in sorted
order (from smallest to largest). Use the min and max functions to find the smallest
and largest values. The middle value can be found by computing the sum of all three
values, and then subtracting the minimum value and the maximum value.
'''
print("Solution to exercise number 32")
try:
    first_input_number : int = int(input("Enter the first number : "))
    second_input_number : int = int(input("Enter the second number : "))
    third_input_number : int = int(input("Enter the second number : "))
    number_list : list[int] = [first_input_number,second_input_number,third_input_number]
    max_number : int = max(number_list)
    min_number : int = min(number_list)
    middle_number_list : list[int] = [number for number in number_list if number != max_number and number != min_number]
    print(f"Max number is : {max_number}")
    print(f"The middle number is : {middle_number_list[0]}")
    print(f"The minimun number is : {min_number}")

except ValueError:
    print("Invalid Input")