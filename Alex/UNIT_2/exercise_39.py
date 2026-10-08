import sys
'''
Exercise 39:SoundLevels
(30 Lines)
The following table lists the sound level in decibels for several common noises.

Noise --- Decibellevel(dB)
Jackhammer --- 130
Gas lawnmower --- 106
Alarm clock --- 70
Quiet room --- 40

Write a program that reads a sound level in decibels from the user. If the user
enters a decibel level that matches one of the noises in the table then your program
should display a message containing only that noise. If the user enters a number
of decibels between the noises listed then your program should display a message
indicating which noises the level is between.Ensure that your program also generates
reasonable output for a value smaller than the quietest noise in the table, and for a
value larger than the loudest noise in the table.

'''

sound_levels : dict[str,int]= {130 : "Jackhammer" ,106 : "Gas lawnmower",70 : "Alarm clock",40 : "Quiet room"}
sound_levels_values : list[int] = list(sound_levels.keys())

try:
    #1.- User input
    sound_level_input : int = int(input("Enter the value of the noise [dB] : "))

    #2.-Validation, check if user input match any value in the table (dict)
    if sound_level_input in sound_levels_values:
        print(f"The user entered a common level sound : {sound_levels[sound_level_input]}")
        sys.exit()

    #2.-Validation, check if user input in between the values of the table
    if sound_level_input > 40 and sound_level_input < 70:
        print(f"The sound is between {sound_levels[40]} and {sound_levels[70]}")

    elif sound_level_input > 70 and sound_level_input < 106:
        print(f"The spund is between {sound_levels[70]} and {sound_levels[106]}")

    elif sound_level_input > 106 and sound_level_input < 130:
        print(f"The sound is between {sound_levels[106]} and {sound_levels[130]}")
    else:
        print("The entered sound is not in the available range. [40 - 130] dB")

except ValueError as verr:
    print(f"[VALUE ERROR] : {verr}")






