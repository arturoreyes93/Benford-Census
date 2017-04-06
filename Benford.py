#  File: Benford.py

#  Description: reads the concesus data and prints the count of numbers for each leading digit and the their percentage

#  Student Name: Arturo Reyes Munoz

#  Student UT EID: ar48836

#  Course Name: CS 303E

#  Unique Number: 50865

#  Date Created: 04/21

#  Date Last Modified: 04/21

def main():

	pop_freq = {}
	pop_freq [1] = 0
	pop_freq [2] = 0
	pop_freq [3] = 0
	pop_freq [4] = 0
	pop_freq [5] = 0
	pop_freq [6] = 0
	pop_freq [7] = 0
	pop_freq [8] = 0
	pop_freq [9] = 0

	file = open ("./Census_2009.txt", "r")

	header = file.readline()

	total = 0

	for line in file:

		line = line.strip()
		pop_data = line.split()
		pop_num = pop_data[-1]
		pop_freq [int(pop_num[0])] += 1
		total+=1

	print('Digit   Count   %')

	percentage = []
	space = '    '

	for i in range(1,10):
		if len(str(pop_freq[i]))<4:
			space = '     '
		percentage.append(round((pop_freq[i]*100/total),1))
		print(str(i)+'       '+str(pop_freq[i])+space+str(percentage[i-1]))

	file.close()

main()




