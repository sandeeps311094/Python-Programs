#-- Python3.6 solution for Leetcode problem 202: --#

'''
Write an algorithm to determine if a number n is "happy".
A happy number is a number defined by the following process: Starting with any positive integer,
replace the number by the sum of the squares of its digits, and repeat the process until the
number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers.
Return True if n is a happy number, and False if not.
'''


import os
import time
import getpass
import imp

from nltk import *

#------------------
def master_block():
    number = int (input ("\nEnter the number: "))
    string_number = str (number)
    total_count = 0
    flag = 0

    while (string_number != '1'):
        return_ticket, string_number = square (string_number)
        total_count += 1

        if (return_ticket == 'True'):
            breakout()

        if (total_count > len (string_number)):
            flag = -1
            print ("\n\n-------------------------------")
            break

    flag_output (flag)

#--------------------------
def square (string_number):
    final_string = ''
    return_ticket = ''

    i = 0
    while (i < len (string_number)):
        ith_num = int (string_number [i])
        second_str = ith_num * ith_num

        if (i == 0):
            final_string = 0 + int (str (second_str))
        else:
            final_string = int (final_string) + int (str (second_str))

        final_string = str (final_string)
        i += 1

    if (final_string == '1'):
        return_ticket = 'True'
    elif (final_string != '1'):
        return_ticket = 'False'

    return (return_ticket, final_string)


#--------------
def breakout():
    print ("\n\n---------------------")
    flag = 1
    flag_output (flag)
    exit (0)


#----------------------
def flag_output (flag):
    if (flag == 1):
        print ("Number is happy*** \n\n")
    elif (flag == -1):
        print ("Number is NOT happy...... !!!\n\n")


#------------
def parenthesis ():
    valid_flag = None
    par_string = str (input ("\nEnter the string: "))

    list_valid = [40, 41, 91, 93, 123, 125]
    for i in par_string:
        if (ord (i) not in list_valid):
            valid_flag = 'False'
            break

    print ("\n\n\nString --> {}\n\n\n".format (par_string))
    i = 0
    while (i < len (par_string)):
        if ((par_string [i] == '(') and (par_string [i+1] == ')')):
            valid_flag = 'True'
        else:
            valid_flag = 'False'

        if ((par_string [i] == '[') and (par_string [i+1] == ']')):
            valid_flag = 'True'
        else:
            valid_flag = 'False'

        if ((par_string [i] == '{') and (par_string [i+1] == '}')):
            valid_flag = 'True'
        else:
            valid_flag = 'False'

        i += 1

    if (valid_flag == 'True'):
        print ("\n\nValid !")
    elif (valid_flag == 'False'):
        print ("\n\nINVALID.... !!!")


#----------------------------------------------------
''' Leet Code problem number 53. maximum subarray '''

def sub_array ():
    ls = []

    while (1):
        element = str (input ("\nEnter a numeral:   (OR)    'q' to quit.... "))

        if (element == 'q'):
            break
        else:
            ls.append ( int (element))

    """ ABORTED """

#-----------------------------------------------------
''' Leet Code problem number 9. Palindrome number '''

def reverse_int ():
    number = int (input ("\nEnter a number: "))
    str_num = str (number)

    ls = list (str_num)
    ls.reverse()
    reverse_str = ''

    for i in ls:
        reverse_str = reverse_str + i
    reversed_number = int (reverse_str)

    def check_palin (number, reversed_number):
        flag_pal = 0

        if (number == reversed_number):
            flag_pal = 1
        elif (number != reversed_number):
            flag_pal = -1
        else:
            flag_pal = 0

        return (flag_pal)

    flag = check_palin (number, reversed_number)

    if (flag == 1):
        print ("\n{}  AND  {} are palindromes *** \n".format (number, reversed_number))
    elif (flag == -1):
        print ("\n{}  AND  {} are NOT_palindromes... !!\n".format (number, reversed_number))
    elif (flag == 0):
        print ("\nInnapropriate flag identified !\n")
    else:
        print ("\nProgram corrupted !!\n")


#-------------------------
if __name__ == '__main__':
    #master_block()
    parenthesis()

    #reverse_int ()
