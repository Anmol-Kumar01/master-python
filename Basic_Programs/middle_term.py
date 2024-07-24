"""This program is used to find out the middle 3rd term.
Author : Anmol Kumar
Date   : 29 December 2022"""
def middle(text):
	"""Retruns: the 3rd term the string
	the middle function will find out the length of text and divivde by 3rd (round them)
	and continuous till 2/3rd  part of it"""

	size=len(text)
	first=size//3
	end=2*size//3
	x=text[first:end]
	return x
print(middle("It is a nice day today"))
