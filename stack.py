#---- This program demonstrates a stack of integers ----#




#========================

class Stack:
    points = 12

    def __init__ (self):
        self.stack = []
        self.limit = 7
        self.expansion_units = 3

    def add_front (self):
        length = Stack.size (self)
        if (length > self.limit):
            print ("\n\nStack full... !")
        else:
            element = int (input ("\nEnter the integer: "))
            self.stack.insert (0, element)

    def add_rear (self):
        if (length > self.limit):
            print ("\n\nStack full... !")
        else:
            element = int (input ("\nEnter the integer: "))
            self.stack.append (element)

    def remove_front (self):
        try:
            self.stack.remove (self.stack [0])
        except:
            print ("\n\nStack is empty !!")

    def remove_rear (self):
        try:
            self.stack.pop ()
        except:
            print ("\n\nStack is empty !!")

    def display (self):
        print ("\nStack --> {}\n".format (self.stack))

    def len (self):
        length = Stack.size (self)
        print ("\n\nLENGTH ---> {}\n\n\n".format (length))

    def size (self):
        size = len (self.stack)
        return (size)

    def expand (self):
        self.limit = 10
        print ("\nStack expanded, Size --> {}".format (self.limit))

    def compress (self):
        if (self.limit == 10):
            self.limit = 7
        elif (self.limit == 7):
            self.limit = 5
        else:
            print ("\n\nStack corrupt !!!\n")
        print ("\nStack compressed, Size --> {}".format (self.limit))

#=====================

class Queue:
    points = 12

    def __init__ (frame):
        frame.que = []
        limit = 7

    def insert (frame):
        ele = str (input ("\n\nInsert char: "))
        frame.que.append (ele)

    def filter (frame):
        for i in frame.que:
            if (ord (i) == 64):
                print ("\n\n++++")
            else:
                continue

#======================
