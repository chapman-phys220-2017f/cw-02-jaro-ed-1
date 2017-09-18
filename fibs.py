#!/usr/bin/env python3

def fibs(n):
	f_list = [1,1];           ### no semicolons. DO NOT USE TABS. Use 4 spaces to indent.
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

###
# The following code should be in a __main__ block. Do not put executable code outside of a
# main block. You want to import the module, and use the functions above directly. If you want
# a convenience function that does the below actions, put it in a function and call that function
# explicitly when needed.
###

fibs_list = fibs(5);
print(fibs_list)

g = fib_generator()
print([next(g) for _ in range(5)])
