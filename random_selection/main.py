##########################################################################
#
#    Tufts University, Comp 160 randSelect coding assignment  
#    main.py
#    randomized selection
#
#    simple main to test randSelect
#    NOTE: this main is only for you to test randSelect. We will compile
#          your code against a different main in our autograder directory
#
##########################################################################

from randSelect import randSelect


def main():
	v = [3,3,3,3, 4, 5, 1, 2]
	rankWeWant = 8
	ourNumber = randSelect(v, rankWeWant)
	#expectedNumber = sorted(v)[rankWeWant]
	#print expectedNumber
	#if ourNumber != expectedNumber :
	#	print "Nooo!"
	#else:
	#	print "Yayy!"


if __name__ == '__main__':
	main()