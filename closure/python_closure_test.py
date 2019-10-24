#!/usr/bin/env python
def make_addr(x):
	def add(y):
		return x+y
	return add


add5 = make_addr(5)
add10 = make_addr(10)

print add5(7)

print "***********"

print make_addr(1)(2)

print "***********"

print "both the parsing the parameter of make_addr(1)(2)(3) or make_addr(1) will throw an exception"
