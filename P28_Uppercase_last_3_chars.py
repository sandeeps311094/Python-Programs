#---  In this program, a word is input and the last three characters are printed in upper case.


import os
import time

def main():
	str1 = str(input("Enter a string: "))		#-- Input a string
	ls1 = []				#-- Initialize an array

	if (len(str1) < 3):


		for i in str1:
			ls1.append(i)		#-- Converting string to array

	ls1.reverse()		#-- Reversing the array so ['a', 'b', 'c'] --> ['c', 'b', 'a']
	ls2 = []			#-- Initialize another empty array to store last 3 charecters

	iterator = 0
	while(iterator < 3):
		ls2.append (ls1[iterator])		#-- Appending the last 3 charecters on str1 to ls2
		iterator += 1

	ls2.reverse()	#-- Since the 3 charecters are in reverse order, we get them back to normal
	str2 = ""		#-- Initialize another empty string to store last 3 charecters

	for i in ls2:
		str2 = str2 + i 	#-- Last 3 charecters from array to string

	ls1.reverse()		#-- Reversing the charecters again  
	
	iterator = 1
	while(iterator <= 3):	#-- Removing the last 3 charecters from str1 so we can append it with new str2
		ls1.pop()			#-- pop() deletes the last charecter in the array
		iterator += 1

	str1 = ""				#-- Overriding the string str1 to empty string
	for i in ls1:
		str1 = str1 + i  	#-- Converting the list/array to string

	str3 = ""			#--- A new empty string is initialized to hold CAPITAL alphabets
	iterator = 0

	while (iterator < 3):
		str3 = str3 + chr(ord(str2[iterator]) -  32) #-- Converting lowercase to upparcase 
		iterator += 1

	str_fin = ""			#-- A final string to store the last 3 CAPITAL alphabets
	str_fin = str1 + str3	#-- Updating the final string

	time.sleep(0.5)
	print ("Final string --> ", str_fin)

#--

if __name__ == '__main__':
	main()





