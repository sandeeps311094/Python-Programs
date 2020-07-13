#---- Circular Queue demo ----#



def circular_queue ():
    cirq = []
    pointer = 0
    size = 0

    def insert (circ, pointer, size):
        if (size > 7):
            print ("\nCircular Queue full !!\n")
        else:
            element = int (input ("\nEnter an integer: "))
            cirq.insert (pointer, element)
            size += 1

            if (pointer == 6):
                pointer = 0
            else:
                pointer += 1

    #--

    def remove (cirq, pointer, size):
        if (size <= 0):
            print ("\nCirculat Queue empty.. !!\n")
        else:
            cirq.remove (cirq [pointer])
            size -= 1
            if (pointer == 0):
                pointer = 7
            else:
                pointer -= 1

    #--

    def display (cirq, pointer, size):
        print ("\n\nCirc Queue --> {}\n\nPointer --> {}\n\nSize --> {}\n".format (cirq, pointer, size))

if __name__ == '__main__':
    circular_queue ()
