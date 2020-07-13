#---  The program takes into input a few numbers by choice of the user. Any negative number present in the list will be printed along with its square.


import os
import time

def main():
	ls_array = []

	while(1):
		choice = str(input("Press 'Y' or 'y' if you wish to add another element into the array. Else press 'N'"))  #-- Take an input as to whether or not you want to append another number into your list/array
		if (choice == 'y' or choice == 'Y'):
			element = int(input("Enter your number: "))	#-- Take inputs into the list/array
			ls_array.append(element)

		elif (choice == 'n' or choice == 'N'):	#-- If choice is 'No' then exit out of the loop
			break

	find_negative(ls_array)		#-- Function call to find the negative element in the loop

#--

def find_negative(ls_array):
	for i in ls_array:
		if (i < 0):
			print ("\nThe negative number caught is --> ", i)
			square = (i * i)									#-- If a negative number is caught, print the square of that number

			print ("The square of the number is --> ", square)
			i += 1

		else:
			i += 1

#--

if __name__ == '__main__':
	main()
