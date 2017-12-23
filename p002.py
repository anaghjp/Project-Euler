#! /usr/bin/python
# -*- coding: utf-8 -*-


def foo():
	even_sum = 0
	s1, s2 = 1, 2
	while(s1 < 4000000):
		even_sum += s1 if s1 % 2 == 0 else 0
		s1, s2 = s2, s1 + s2
	print even_sum


if __name__ == '__main__':
	foo()
