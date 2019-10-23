#!/usr/bin/env python
from quick_sort import q_sort

def main():
	v = [10, 7, 8, 9, 1, 5]
	rankWeWant = 8
	array = q_sort(v)
	#expectedNumber = sorted(v)[rankWeWant]
	#print expectedNumber
	#if ourNumber != expectedNumber :
	#	print "Nooo!"
	#else:
	#	print "Yayy!"
	print (array)


if __name__ == '__main__':
	main()