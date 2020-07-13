#--- This program prints name of the last alphabet in digit

import os
dc_digit = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four',
			5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 
			9: 'Nine', 0: 'Zero'}

def main():
	num = int(input("Enter a digit: "))
	last_digit = (num % 10)

	name_of_last_digit = dc_digit[last_digit]
	print ("Name --> ", name_of_last_digit)

#--

if __name__ == '__main__':
	main()

#----------------------------

