#!/usr/bin/env python3

import scipy                ### Not needed, so remove

def compute_sum(tol=1e-2):
	sum = 0;                            ### No semicolons needed
	k = 1;
	diff = 1;
	while diff >= tol:
		sum_save = sum;             
		sum += 1/k**2;               
		diff = sum - sum_save;      ### How did you know this would be positive?
		k += 1;
	return sum

str_tol = input("What tolerance will you accept? ")
usr_tol = float(str_tol);
lim = compute_sum(usr_tol);
print(lim)		
