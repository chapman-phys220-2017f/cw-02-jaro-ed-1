#!/usr/bin/env python3

import scipy

def compute_sum(tol=1e-2):
	sum = 0;
	k = 1;
	diff = 1;
	while diff >= tol:
		sum_save = sum;
		sum += 1/k**2;
		diff = sum - sum_save;
		k += 1;
	return sum

str_tol = input("What tolerance will you accept? ")
usr_tol = float(str_tol);
lim = compute_sum(usr_tol);
print(lim)		
