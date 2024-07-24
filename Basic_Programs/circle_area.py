"""This program is used to check the area of two circles whose radius is given.
Author : Anmol
Date   : 20 December 2022"""

def circle_area(radius1,radius2):
	"""Returns : the sum of area of two circles also give information about their size

	Parameter radius1 : radius1 is the radius of first circle
	Precondition      : radius1 is either float or int type value
	Parameter radius2 : radius2 is the radius of the second circle
	Precondition      : radius2 is either float or int type value

	example:
	>>> circle_area(5,1)
	81.64
	Medium
	>>> circle_area(2,10)
	326.56
	High
	>>> circle_area(1,3)
	31.400000000002
	"""
	area1=(3.14)*radius1**2
	area2=(3.14)*radius2**2
	print(area1+area2)
	if area1+area2 >= 100:
		return "High"
	elif 50 < area1+area2 < 100:
		return "Medum"
	elif area1+area2<50:
		return "Low"
a=circle_area(1,3)
print(a)	
