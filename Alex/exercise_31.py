'''
Exercise 31: Sum of the Digits in an Integer
(18 Lines)
Develop a program that reads a four-digit integer from the user and displays the sum
of the digits in the number. For example, if the user enters 3141 then your program
should display 3 + 1 + 4 + 1 = 9.
'''
print("Solution to exercise number 31")
try:
    number : int = int(input("Enter a integer number (four digits only) :"))
    number_string : str = str(number)
    if(len(number_string) > 4):
        raise ValueError
    number_list : list[int] =  list(map(int, list(number_string)))
    
    result_string : str = ""
    for i in number_string:
        result_string = result_string + i + " + "
    print(f"Result : {result_string} = {sum(number_list)}")


except ValueError:
    print("Error, tyope just 4 digits...")
