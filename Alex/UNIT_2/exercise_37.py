from enum import Enum
'''
Exercise 37:NamethatShape
(Solved—31 Lines)
Write a program that determines the name of a shape from its number of sides. Read
the number of sides from the user and then report the appropriate name as part of
a meaningful message. Your program should support shapes with anywhere from 3
up to (and including) 10 sides. If a number of sides outside of this range is entered
then your program should display an appropriate error message.
'''


class Shape(Enum):
    TRIANGLE = 3
    SQUARE = 4
    PENTAGON = 5
    HEXAGON = 6
    HEPTAGON = 7
    OCTAGON = 8
    NONAGON = 9
    DECAGON = 10

    

try:
    number_of_sides : int = int(input("Enter th number of sides : "))
    if number_of_sides < 3 or number_of_sides > 10 :
        raise ValueError("[ERROR]: The number of sides must be between 3 and 10")
    match number_of_sides:
        case 3:
            print(f"The shape is : {Shape(3).name}")
        case 4:
            print(f"The shape is : {Shape(4).name}")
        case 5:
            print(f"The shape is : {Shape(5).name}")
        case 6:
            print(f"The shape is : {Shape(6).name}")
        case 7:
            print(f"The shape is : {Shape(7).name}")
        case 8:
            print(f"The shape is : {Shape(8).name}")
        case 9:
            print(f"The shape is : {Shape(9).name}")
        case 10:
            print(f"The shape is : {Shape(10).name}")
    
except ValueError as verr:
    print(f"[VALUE ERROR] - {verr}")