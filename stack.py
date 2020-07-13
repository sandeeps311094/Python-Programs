#--  A demonstration of a double-ended queue datastructure using Python


import os
import time

class Stack:

    def __init__(self):
        self.stack = []
        self.size = 5
        self.i_count = 0
        self.d_count = 0

    def add_front(self):
        element = input("Enter the element: ")

        if (len(self.stack) >= self.size):
            time.sleep(0.8)
            print ("Stack is full !")
        else:
            self.stack.insert (0, element)
            self.i_count += 1

    def add_rear(self):
        element = input("Enter the element: ")

        if (len(self.stack) >= self.size):
            time.sleep(0.8)
            print ("Stack is full !")
        else:
            self.stack.append(element)
            self.i_count += 1

    def remove_front(self):
        if (len(self.stack) == 0):
            print ("Stack is empty !")
        else:
            self.stack.remove (self.stack[0])
            self.d_count += 1

    def remove_rear(self):
        if (len(self.stack) == 0):
            print ("Stack is empty !")
        else:
            self.stack.pop()
            self.d_count += 1

    def display(self):
        time.sleep(0.8)
        print ("Current Stack --> {}".format (self.stack))

    def expand(self):
        if (self.size > 9):
            print ("Stack size max limit reached !")
        elif (self.size <= 9):
            self.size += 2

    def compress(self):
        if (self.size < 5):
            print ("Stack size min limit reached !")
        elif (self.size <= 5):
            self.size -= 2

    def check_valid_stack(self):
        time.sleep (0.8)
        if ((self.stack  == []) and (self.i_count == self.d_count)):
            print ("VALID")

        elif ((self.stack  != []) and (self.i_count == self.d_count)):
            print ("INVALID... !")

        elif ((self.stack  == []) and (self.i_count != self.d_count)):
            print ("INVALID... !")

        elif ((self.stack  != []) and (self.i_count != self.d_count)):
            print ("VALID")


#---------------------

class Queue(object):

    def __init__(self):
        self.queue = []
        self.queue_size = 7
        self.i_count = 0
        self.d_count = 0

    def insert(self):
        element = input ("Enter element: ")

        if (len(self.queue) >= self.queue_size):
            time.sleep(0.8)
            print ("Queue is full !")
        else:
            self.queue.insert (0, element)
            self.i_count += 1


    def remove(self):

        if (len(self.queue) == 0):
            print ("Stack is empty !")
        else:
            self.queue.pop()
            self.d_count += 1


    def display(self):
        time.sleep(0.8)
        print ("Current Queue --> {}".format(self.queue))


    def check_valid_queue(self):
        time.sleep(0.8)
        if ((self.stack == []) and (self.i_count == self.d_count)):
            print ("VALID")

        elif ((self.stack != []) and (self.i_count == self.d_count)):
            print ("INVALID... !")

        elif ((self.stack == []) and (self.i_count != self.d_count)):
            print ("INVALID... !")

        elif ((self.stack != []) and (self.i_count != self.d_count)):
            print ("VALID")


#---------------------

class stack(object):

    def __init__(self):
        self.stack = []
        self.size = 7
        self.i_count = 0
        self.d_count = 0

    def push(self):
        element = input("Enter element: ")

        if (len(self.stack) >= self.size):
            time.sleep(0.8)
            print ("Stack is full !")
        else:
            self.stack.insert(0, element)
            self.i_count += 1


    def pop(self):
        if (len(self.stack) <= self.size):
            time.sleep (0.8)
        else:
            self.stack.pop()
            self.d_count += 1


#---------------------

if __name__ == '__main__':
    stk = stack.Stack()
