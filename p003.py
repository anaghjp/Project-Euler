#! /usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
from eulerlib import is_square, primes


def foo():
	num = 600851475143
	is_sq, sqrt = is_square(num)
	primes_list = primes(sqrt + 1)
	for x in reversed(primes_list):
		if num % x == 0:
			print x
			return
	print num


if __name__ == '__main__':
	foo()
