#--- This program accepts a range of numbers and prints the sum of all prime numbers in that range


import os

def main():
	n = int(input("Enter the starting range: "))		#-- Input starting range
	m = int(input("Enter the ending range: "))		#-- Input ending range

	i = n
	total = 0					#-- Initialize this variable to calculate the total of all prime numbers in the range
	while (i <= m):
		if isprime(i):				#-- Function call to check if the number is prime or not
			total = total + i
		i += 1

	print ("Total --> ", total)

#--

def isprime(element):
	count = 0					#-- This variable counts the total numbers that are divisible by the main number

	i = 2
	while(i <= element):
		if (element % i == 0):		#-- Checking for prime or not
			count += 1
		i += 1

	if (count > 1):				#-- Not prime so return False
		return False

	elif (count == 1):
		return True				#-- Prime so return True

	else:
		pass			#-- A special case where if the count by mistake goes to negative, then it returns nothing
						#-- NOTE --> 'Pass' does not return anything
#--

if __name__ == '__main__':
	main()
	
	
