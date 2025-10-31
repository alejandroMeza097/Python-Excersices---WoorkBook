'''
Exercise 24: Units of Time
(22 Lines)
Create a program that reads a duration from the user as a number of days, hours,
minutes, and seconds. Compute and display the total number of seconds represented
by this duration.
'''
print("Solution to exercise number 24")
try:
    DAYS_TO_HOURS : int = 24
    HOURS_TO_MINUTES : int = 60
    MINUTES_TO_SECONDS : int = 60

    days : int = int(input("Enter the amout of days : "))
    hours : int = int(input("Enter the amout of hours : "))
    minutes : int = int(input("Enter the amount of minuts : "))
    seconds : int = int(input("Enter the amount of seconds : "))

    days_to_seconds : int = days * DAYS_TO_HOURS * HOURS_TO_MINUTES * MINUTES_TO_SECONDS
    hours_to_seconds : int = hours * HOURS_TO_MINUTES * MINUTES_TO_SECONDS
    minutes_to_seconds : int = minutes * MINUTES_TO_SECONDS

    total_seconds : int = days_to_seconds + hours_to_seconds + minutes_to_seconds + seconds

    print(f"The total of seconds is : {total_seconds} segundos")

except ValueError as val_err:
    print(f"[ERROR] An error just ocurred {val_err}")