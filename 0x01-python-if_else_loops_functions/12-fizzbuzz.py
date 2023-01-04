#!/usr/bin/python3
def fizzbuzz():
    result = ""
    for i in range(1, 101):
        if i % 5 == 0 and i % 3 == 0:
            result += "FizzBuzz "
        elif i % 5 == 0:
            result += "Buzz "
        elif i % 3 == 0:
            result += "Fizz "
        else:
            result += str(i) + " "
    print(result, end="")
