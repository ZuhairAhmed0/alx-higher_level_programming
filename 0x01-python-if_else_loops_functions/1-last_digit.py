#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit= str(number)[-1]
if number > 5:
    stri = f"{last_digit} and is greater than 5"
elif number == 0:
    stri = f"{last_digit} and is 0"
elif number < 6 and not 0:
    stri = f"-{last_digit} and is less than 6 and not 0"
print(f"Last digit of {number} is {stri}")
