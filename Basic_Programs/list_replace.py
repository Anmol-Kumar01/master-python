"""This program will return the replaced list with the average of it's neighbour
Author : Anmol Kumar
Date   : 3 january 2023
"""
a=[2,3,4]
def list_replace(a):
	b=[]
	for x in a:
		b=b.append((x+1)/2)
		return b
print(list_replace(a))
		
