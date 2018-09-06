"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

request = input(" ")

while True:
    split_request = request.split(" ")

    if split_request[0] == 'q':
        
        break
        
    break