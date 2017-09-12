#!/usr/bin/env python3

def coord_for(n, a=0, b=1):
	list = [];
	length = (b-a)/n;
	for num in range (0,n+1):
		x= num*length + a;
		list.append(x);
	return list

def coord_while(n, a=0, b=1):
	list = [];
	length = (b-a)/n;
	c = 0;
	while c < n+1:
		x= c*length + a;
		list.append(x);
		c= c+1;
	return list

def coord_comp(n, a=0, b=1):
	length = (b-a)/n;
	list = [i*length for i in range(n+1)];
	return list

num_int = 5;
c_for = coord_for(num_int);
print(c_for)
c_while = coord_while(num_int);
print(c_while)
c_comp = coord_comp(num_int);
print(c_comp)
print("Split into "+str(num_int)+" intervals.")
