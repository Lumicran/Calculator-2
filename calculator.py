"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

request = input(" ")

while True:
    split_request = request.split(" ")
    first = split_request[0]

    num1 = int(split_request[1])
    num2 = int(split_request[2])

    if first == 'q':
        break
        
    elif first == "+":
        print(add(num1, num2))


    break


