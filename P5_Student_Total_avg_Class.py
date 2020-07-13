#--  A simple student marks card report program


import os
import time

def main():
	os.system('clear')
	name = str(input("Enter name: "))
	math = int(input("Enter math score: "))
	science = int(input("Enter science score: "))
	music = int(input("Enter music score: "))

	total, avg = calc_avg(math, science, music)

	grade = calc_class(total)

	print ("Total --> ", total)
	print ("Average --> ", avg)
	print ("Class --> ", grade)

#--

def calc_avg(math, science, music):
	total = (math + science + music)
	avg = (total / 3)

	time.sleep(1.0)
	return total, avg

#--

def calc_class(total):
	grade = ""

	if (total >= 90):
		grade = "Excellent"

	elif (total >= 80 and total < 90):
		grade = "Very Good"

	elif (total >= 70 and total < 80):
		grade = "Good"

	elif (total >= 60 and total < 70):
		grade = "Satisifactory"

	elif (total >= 50 and total < 60):
		grade = "Bad"

	elif (total >= 40 and total < 50):
		grade = "Fail"

	elif (total == 0):
		grade = "Royally Fucked Up !!!"

	else:
		grade = "Go Fuck Yourself !!!"

	return grade

#--

if __name__ == '__main__':
	main()


