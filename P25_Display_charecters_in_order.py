#---  This program accepts a word and prints all the alphabets in an alphabetic order


import os

def main():
	word = str(input("Enter the word: "))		#-- Taking an input from user

	ordered_word = ordered_chars(word)			#-- Calling the function to sort the charecters in order

	print ("Ordered word --> ", ordered_word)

#--

def ordered_chars(words):
	ls_ASCII = []					#-- Initialize a list/array to store the ASCII values

	for element in words:
		ls_ASCII.append(ord(element)) 	#-- The 'ord' function will convert character into its ASCII value

	ls_ASCII.sort()				#-- The ASCII values in the list/array are sorted

	ordered_word = ""			#-- Initialize an empty string to store the ordered words

	for element in ls_ASCII:
		ordered_word = ordered_word + chr(element)	#-- The 'chr' function converts an ASCII number back to charecter. Reverse of 'ord'

	return ordered_word

#--

if __name__ == '__main__':
	main()

