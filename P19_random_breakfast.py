#---  This program takes as user input a few breakfast names. It asks a choice of whether or not you want to pick one breakfast randomly. If 'yes', it randomly picks a breakfast. If 'no' then the program exits.


import time
import random

def main():
	ls_breakfast = []					#-- This is a datastructure to hold an array of 6 breakfast names
	iterator = 1				#-- Similar to assigning 'i=0' for the loop

	while(iterator <= 6):
		bf = input("Enter a breakfast: ")		#-- Takes input of user generated breakfasts
		ls_breakfast.append (str(bf))			#-- Inputs the user generated breakfast name into the datastructure
		iterator += 1

	print ("Breakfast list: ", ls_breakfast)	#-- Printing the list
	random_bf(ls_breakfast)						#-- This is a function call to function random_bf()

#--

def random_bf(ls_breakfast):
	while(1):
		time.sleep(1.4)
		choice = input("Do you want to generate another random value ? ") #-- Choice of input
		if ((choice == 'Y') or (choice == 'y') or (choice == 'yes') or (choice == 'Yes')):
			rand = random.choice(ls_breakfast)			#-- The random function chooses one value from the list
			print ("Random breakfast --> ", rand)	

		elif ((choice == 'N') or (choice == 'n') or (choice == 'no') or (choice == 'No')):
			break

#--

if __name__ == '__main__':
	main()								#-- Generating the program

