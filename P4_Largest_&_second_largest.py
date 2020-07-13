#--  This program inputs three numbers and outputs the largest and second largest of the nnumbers

import os

def main():
	iterator = 1
	ls_num = []

	while(iterator <= 3):
		num = int(input("Enter the number: "))
		ls_num.append(num)
		iterator += 1

	ls_num.sort()
	ls_num.reverse()

	largest = ls_num[0]
	second_largest = ls_num[1]

	print ("Largest --> ", largest)
	print ("2nd Largest --> ", second_largest)

#--

if __name__ == '__main__':
	main()


