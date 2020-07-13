""" This Python3.6 Program takes an input and outputs the following triangle:

    Input:  5

    Output: A
            BA
            CBA
            DCBA
            EDCBA
"""

#-----------
def list_alphabets ():              #--  This method creates a list of alphabets ans returns a reversed list
    ls = []
    i = 65
    while (i <= 90):
        ls.append (chr (i))         #-- Making use of the ASCII values to generate each character
        i += 1
    ls.reverse ()
    main (ls)

#-----------
def main (ls):
    lines = int (input ("\nEnter the number of lines: "))   #-- Taking the number of lines as input from the user
    print ("\n\n")
    key_element = ''

    i = 0
    while (i < lines):                          #-- This loop generates the triangle of Characters required
        key_element = key_element [::-1] + (ls [len (ls) - (i+1) ])
        key_element = key_element [::-1]
        print ("{}".format (key_element))
        i += 1

#-----------
if __name__ == '__main__':
    list_alphabets ()
