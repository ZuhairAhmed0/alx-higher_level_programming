#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit= int(str(number)[-1])
if digit > 5:
    str = f"{digit} and is greater than 5"
elif digit == 0:
    str = f"{digit} and is 0"
elif digit < 6 and not 0:
    str = f"-{last_digit} and is less than 6 and not 0"
print(f"Last digit of {number} is {str}")
