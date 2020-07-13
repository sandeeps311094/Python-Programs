#---- Hacker Rank Demo program_1
''' Given a string 'S' and width 'w', you seperate a string using the w and print the rest in the next line.
'''

def main ():
    string = str (input ("Enter a string: "))
    width  = int (input ("Enter the width: "))

    i = 0
    while (i < len (string)):
        if (((i) % width) == 0):
            print ("\n")
            print (string [i], end = "")
            i += 1

        else:
            print (string [i], end = "")
            i += 1
 
    print ("\n\n")

main()


