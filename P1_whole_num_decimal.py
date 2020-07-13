#-- The below Python code inputs a float number, and outputs both the numeral and decimal values.

import os

def main():
	os.system('clear')
	num = float(input("Enter a whole number with decimal: "))	#-- Taking an input

	decimal = (num - int(num))			#-- Extracting only decimal part of the whole number 
	decimal = round(decimal, 4)			#-- Rounding off the decimal. You can round off to any number

	num_int = int (num)					#-- Extracting only numeral value

	print ("Decimal value --> ", decimal)
	print ("Integer value --> ", num_int)	#-- Printing

#--

if __name__ == '__main__':
	main()
