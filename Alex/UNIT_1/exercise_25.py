'''
Exercise 25: Units of Time (Again)
(Solved—24 Lines)
In this exercise you will reverse the process described in the previous exercise.
Develop a program that begins by reading a number of seconds from the user.
Then your program should display the equivalent amount of time in the form
D:HH:MM:SS, where D, HH, MM, and SS represent days, hours, minutes and sec-
onds respectively. The hours, minutes and seconds should all be formatted so that
they occupy exactly two digits, with a leading 0 displayed if necessary
'''
print("Solution to exercise number 25")

try:
    DAYS_TO_HOURS : int = 24
    HOURS_TO_MINUTES : int = 60
    MINUTES_TO_SECONDS :int = 60

    seconds : int = int(input("Enter the amount of seconds :"))

    days : int = int(seconds/(DAYS_TO_HOURS * HOURS_TO_MINUTES * MINUTES_TO_SECONDS))
    residuo_seconds = seconds - int(days * (DAYS_TO_HOURS * HOURS_TO_MINUTES * MINUTES_TO_SECONDS))

    hours =  int(residuo_seconds / (HOURS_TO_MINUTES * MINUTES_TO_SECONDS))
    residuo_seconds = residuo_seconds - int( hours  * (HOURS_TO_MINUTES * MINUTES_TO_SECONDS))

    minutes = int(residuo_seconds / MINUTES_TO_SECONDS)
    residuo_seconds =  residuo_seconds - int(minutes * (MINUTES_TO_SECONDS))

    seconds = residuo_seconds
    
    if(hours < 10):
        hours_to_string = f"0{hours}"
    else:
        hours_to_string = f"{hours}"
    
    if(minutes < 10):
        minutes_to_string = f"0{minutes}"
    else:
        minutes_to_string = f"{minutes}"

    if(seconds < 10):
        seconds_to_string = f"0{seconds}"
    else:
        seconds_to_string = f"{seconds}"

    print(f"RESULT: {days}:{hours_to_string}:{minutes_to_string}:{seconds_to_string}")

except ValueError as valErr:
    print(f"An error just ocurred. {valErr}")