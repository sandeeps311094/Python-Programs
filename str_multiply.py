#-- Leetcode problem number_ : The objective of this program is to multiply two numbers as strings and print their product in a string format.

import os
from string import *

def multiplier ():
    str1 = str (input ("\nEnter 1st number: "))
    str2 = str (input ("\nEnter 2nd number: "))

    try:
        num1 = int (str1)
    except:
        print ("\nPlease input a valid 1st number !!")
        exit (0)

    try:
        num2 = int (str2)
    except:
        print ("\nPlease input a valid 2nd number !!")
        exit (0)

    product = (num1 * num2)
    str_prod = str (product)

    print ("\n\nThe product of  {}  &  {}  is -->  {}  and it's data-type is: {}\n".format (num1, num2, str_prod, type (str_prod)))

#--
if __name__ == '__main__':
    multiplier ()
