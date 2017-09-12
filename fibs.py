#!/usr/bin/env python3

def fibs(n):
	f_list = [1,1];
	a,b = 1,1;
	for num in range(2,n):
		a,b = b,a+b;
		f_list.append(b);
	return f_list

def fib_generator():
	a,b = 1,1;
	while True:
		yield a
		a,b = b, a+b;


fibs_list = fibs(5);
print(fibs_list)

g = fib_generator()
print([next(g) for _ in range(5)])
