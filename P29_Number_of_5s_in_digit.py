#---  This program prints the occurences of '5' in a number.


import math

def main(number, count):
	left_digit = int(number / 10)		#-- This generates the number without the last digit
	last_digit = (number % 10)			#-- This gives the last digit of the number

	if (last_digit == 5):			#-- Checking for the occurances of 5
		count += 1

	if (left_digit != 0):
		main(left_digit, count)		#-- This is a reccursice function. If number is not 0, it calls itself again
	else:
		print ("Number of occurances of '5' is --> ", count)

#--

def easy_method(number):
	string = str(number)
	count = string.count('5')

	print ("Number of occurances of '5' is --> ", count)

#-- 

if __name__ == '__main__':
	
	number = int(input("Enter a number: "))		#-- GLOBAL Variable
	count = 0						#-- GLOBAL Variable

	main(number, count)				#-- Making the function call to main() with the 2 global variables
	easy_method(number)

