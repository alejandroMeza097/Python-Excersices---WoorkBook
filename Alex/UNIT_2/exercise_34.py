import logging

'''
Exercise 34: Even or Odd?
(Solved—13 Lines)
Write a program that reads an integer from the user. Then your program should
display a message indicating whether the integer is even or odd
'''
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

try:
    logger.info("Program started")
    input_number : int = int(input('Type an integer number : '))
    if input_number % 2 == 0:
        print(f"Typed number :{input_number} is even")
    else:
        print(f"Typed number :{input_number} is odd")
except ValueError as ver:
    logger.error(f"{ver}")