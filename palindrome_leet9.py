#-- Solution to Leet code problem-9. The objective of this program is to find if a number is palindrome or not.

import os
def reverse_int ():
    number = int (input ("\nEnter a number: "))         #-- Take a non-zero integer as input
    str_num = str (number)                              #-- Convert the integer to a string
    ls = list (str_num)

    if (ls [0] == '0'):                         #-- This function is used to remove all the zeros at the starting of the string. It removes the zeros from the list containing strings
        ls = remove_zero (ls)

    ls.reverse()
    reverse_str = ''

    for i in ls:
        reverse_str = reverse_str + i
    reversed_number = int (reverse_str)

    def check_palin (number, reversed_number):      #-- This function checks if the number is a palindrome or not
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

    def remove_zero (list_num):                 #-- This function removes all unwanted zeros at teh start of the string by taking the list form of the string
        i = 0
        while (i < len (list_num)):
            if (list_num [i] == '0'):
                list_num.remove (list_num [i])
            i += 1
        return (list_num)

#----
if __name__ == '__main__':
    os.system ('clear')
    reverse_int ()
