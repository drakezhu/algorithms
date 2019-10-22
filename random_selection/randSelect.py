##########################################################################
#
#    Tufts University, Comp 160 randSelect coding assignment  
#    randSelect.py
#    randomized selection
#
#    includes functions provided and function students need to implement
#
##########################################################################


# TODO: implement this function
# ray is a list of ints
# index is an int
import random
def randSelect(ray, index):
	if index > len(ray) or index == len(ray):
		raise ValueError("Rank value out of length!")
	print ("Looking for value with rank " + str(index) + " in the array:")
	print (ray)

	# generate random number
	randNum = ray[random.randint(0,len(ray)-1)]

	# doing partition
	sub_1, sub_2, randRank,identical_num = partition(ray, randNum)

	# three situation doing recursion

	if (randRank == index  or randRank < index ) and (randRank + identical_num -1 == index or randRank + identical_num -1 > index):
		print ("Selected " + str(randNum) + " as the pivot; its rank is " + str(randRank) + " Thus, we recurse on nothing. We are done")
		return randNum
	if randRank < index:
		print ("Selected " + str(randNum) + " as the pivot; its rank is " + str(randRank) + " Thus, we recurse on right")
		return randSelect(sub_2, index-randRank)
	if randRank > index:
		return randSelect(sub_1, index)
		print ("Selected " + str(randNum) + " as the pivot; its rank is " + str(randRank) + " Thus, we recurse on left")

	return 0

def partition(ray, num): 
	sub_1 = []
	sub_2 = []
	counter = 0
	identical_num = 0

	for i in ray:
		# number less than random generated number will goes to sub array 1
		if i < num:
			sub_1.append(i)
			counter += 1
		# otherwise go to sub array 2
		if i > num or i == num:
			sub_2.append(i)
		# record the amount of identical generated random number
		if i == num:
			identical_num += 1

	return sub_1, sub_2, counter, identical_num