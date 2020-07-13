#-- The objective of this program is to accept a list of numbers, square them and put them into another list. Then the latter list has to be sorted in ascending order --#

import os
import time as time

def accept_list():
    ls = []
    while (1):
        number = str (input ("\nEnter a number of press 'q' to quit: "))
        if ((number != 'q') and (ord (number [0]) in range (48, 58))):
            ls.append (int (number))
        elif (number == 'q'):
            break
        else:
            print ("\n\nINVALID INPUT...\n\n")
            continue

    print ("\n\nThe entered array is --> {}".format (ls))
    square_list (ls)

#--
def square_list (ls):
    ls_square = []
    for i in ls:
        ls_square.append (i * i)
    print ("\nSquared array --> {}".format (ls_square))

    sort_array (ls_square)

#--
def sort_array (ls_square):
    ls_square.sort ()
    time.sleep (1.25)
    print ("\nSorted squared array --> {}\n".format (ls_square))

#--
def sort (ls):
    ls_sort = []

    i = 0
    while (i < len (ls)):
        j = i + 1
        small = ls [i]
        less  = small
        while (j < len (ls)):
            if ((ls [j] <= small) and (ls [j] <= less)):
                less = ls [j]
                j += 1
            else:
                j += 1
            #ls.remove (ls [ls.index (less)])
        print ("\n\nList: {}".format (ls))
        ls_sort.append (less)
        i += 1

    print ("\n\nSorted array --> {}".format (ls_sort))








#--
if __name__ == '__main__':
    os.system ('clear')
    #accept_list ()

    sort ([3, 7, 12, 8, 1, 5, 0, 14, 6])

""" People beliving whatever they don't know can't exist is the crown of ignorance """