##########################################################################
#
#    Tufts University, Comp 160 wordInterpret coding assignment
#
#    interpret.py
#    wordInterpret
#
#    includes function students need to implement
#
##########################################################################


# TODO: implement this function
# NOTE: please implement this with  Python3. The autograder uses Python3

# inputNums is a string
# function returns an int


d = dict()
for i in range(0,26):
	d[str(i+1)] = chr(ord('a') + i)


def wordInterpret(inputNums):
	#print (d)
	length = len(inputNums)
	if length < 1 or inputNums[0] == '0':
		return 0
	
	if length == 1:
		return 1


	i = 1
	counter = 1
	record = 1
	#for j in range(0,length):
	#	dd[j] = 0
	LastInD = False

	while i < len(inputNums):
		#print(counter)
		temp = counter
		if inputNums[i] == '0' and int(inputNums[i-1]) > 2:
			#print ("Wrong")
			return 0
		elif inputNums[i] == '0':
			#print(counter)
			if lastInD == True:
				counter -= 1


		elif inputNums[i-1] + inputNums[i] in d:
			lastInD = True
			counter += record
		else:
			lastInD = False

		record = temp



		i += 1

	return counter







