"""This function is used to find out the prime number 
Author : Anmol Kumar
Date   : 3 January 2023
"""
#Take the number define the range from 2 till n-1
#check whether it give reminder 0 or not from the range
#if reminder is 0 it is not prime otherwise yes it is prime.

def is_prime(n):
	sqr=int(n**(1/2))
	prime = True
	for x in range (2,sqr+1):
		if n%x==0:
			prime = False
	return prime		
print(is_prime(67))
