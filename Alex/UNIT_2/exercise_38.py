'''
Exercise 38:MonthNametoNumberofDays
(Solved—18 Lines)
The length of a month varies from 28 to 31 days. In this exercise you will create
a program that reads the name of a month from the user as a string. Then your
program should display the number of days in that month. Display “28 or 29 days”
for February so that leap years are addressed
'''

DAYS_OF_THE_MONTHS : dict[str,int | tuple[int,int]] = {"JANUARY":31,"FEBRUARY":(28,29),"MARCH":31,"APRIL":30,
                                                       "MAY":31,"JUNE":30,"JULY":31,"AUGUST":31,"SEPTEMBER":30,
                                                       "OCTOBER":31,"NOVEMBER":30,"DECEMBER":31}
KEYS : list[str] = list(DAYS_OF_THE_MONTHS.keys())


month_input : str = input("Enter the value of the month as text : ")

if month_input.upper() == KEYS[0]:
    print(f"The days of this month are : {DAYS_OF_THE_MONTHS["JANUARY"]}")

elif month_input.upper() == KEYS[1]:
    print(f"The days of this month are : {DAYS_OF_THE_MONTHS["FEBRUARY"][0]} or {DAYS_OF_THE_MONTHS["FEBRUARY"][1]}")

elif month_input.upper() == KEYS[2]:
    print(f"The days of this month are : {DAYS_OF_THE_MONTHS["MARCH"]}")

elif month_input.upper() == KEYS[3]:
        print(f"The days of this month are : {DAYS_OF_THE_MONTHS["APRIL"]}")

elif month_input.upper() == KEYS[4]:
    print(f"The days of this month are : {DAYS_OF_THE_MONTHS["MAY"]}")

elif month_input.upper() == KEYS[5]:
    print(f"The days of this month are : {DAYS_OF_THE_MONTHS["JUNE"]}")

elif month_input.upper() == KEYS[6]:
    print(f"The days of this month are : {DAYS_OF_THE_MONTHS["JULY"]}")

elif month_input.upper() == KEYS[7]:
    print(f"The days of this month are : {DAYS_OF_THE_MONTHS["AUGUST"]}")

elif month_input.upper() == KEYS[8]:
    print(f"The days of this month are : {DAYS_OF_THE_MONTHS["SEPTEMBER"]}")

elif month_input.upper() == KEYS[9]:
    print(f"The days of this month are : {DAYS_OF_THE_MONTHS["OCTOBER"]}")
                    
elif month_input.upper() == KEYS[10]:
    print(f"The days of this month are : {DAYS_OF_THE_MONTHS["NOVEMBER"]}")

elif month_input.upper() == KEYS[11]:
    print(f"The days of this month are : {DAYS_OF_THE_MONTHS["DECEMBER"]}")

else:
    print("No valid month")
    
