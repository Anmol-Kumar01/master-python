def grade(n):
	"""Convert the score card into grades and print it according to the scores
	Parameter n : n is the score
	Precontion  : n is either float or int type value

	examples:
	>>> grade(90)
	A
	>>> grade(85)
	B+
	>>> grade(79)
	B
	>>> grade(59)
	c
	>>> grade(35)
	D
	>>> grade(12)
	F
	>>> grade(-10)
	'Please enter the valid test score'
	"""
	if  100 > n >= 90:
		print("A")
	elif 90 > n >= 80:
	    print("B+")
	elif 80 > n >=60:
	    print("B")
	elif 60 > n >=40:
	    print("C")
	elif 40 > n >=33:
		print("D")
	elif 33 > n >=0:
		print("F")
	else:
		print("Please enter the valid test score")


