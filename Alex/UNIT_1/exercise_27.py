'''
Exercise 27: Body Mass Index
(14 Lines)
Write a program that computes the body mass index (BMI) of an individual. Your
program should begin by reading a height and weight from the user. Then it should
use one of the following two formulas to compute the BMI before displaying it. If
you read the height in inches and the weight in pounds then body mass index is
computed using the following formula:
BMI = (weight /(height * height)) * 703.
If you read the height in meters and the weight in kilograms then body mass index
is computed using this slightly simpler formula:
BMI = weight /(height * height)
'''
print("Solution to exercise number 27")

def bmi_inches_and_pounds (weight,height) -> float:
    try:
        bmi = (weight/(height * height)) * 703
        return bmi
    except Exception as e:
        print(e)


def bmi_meters_and_kilograms (weight,height) -> float:
    try:
        bmi = (weight/(height * height))
        return bmi
    except Exception as e:
        print(e)

try:
    weight_in_pounds : float = float(input("Enter the value of your weight in pounds : "))
    height_in_inches : float = float(input("Enter your height in inches : "))
    print(f"The value of your BMI using pounds and inches is : {bmi_inches_and_pounds(weight_in_pounds,height_in_inches):.5f}")
    weight_in_kilograms : float = float(input("Enter your weight in kilograms : "))
    height_in_meters : float = float(input("Enter your height in meters : "))
    print(f"The value of your BMI using kilograms and meters is : {bmi_meters_and_kilograms(weight_in_kilograms,height_in_meters):.5f}")

except Exception as e:
    print(e)
    



