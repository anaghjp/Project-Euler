#! /usr/bin/python
# -*- coding: utf-8 -*-


def foo():
	s = 0
	for x in xrange(1000):
		if x % 3 == 0 or x % 5 == 0:
			s += x
	print s


if __name__ == '__main__':
	foo()
