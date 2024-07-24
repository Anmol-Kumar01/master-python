"""
This program is used to check the numbers sign
Author : Anmol Kumar
Date   : 15 December 2022
""" 
def pos_neg(num1,num2,negative):
	"""
	Returns True if one is negative and one is positive.
	Except if the parameter "negative" is True, then return True only if both are negative

	Parameter num1 : num1 is a value that is going to be check
	Precondition   : num1 only be of float or int type
	Parameter num2 : num2 is a value that is going to be check
	Precondition   : num2 only be of float or int type
	Parameter negative : num1 is a value that is going to be check
	Precondition   : negative  only be of bool type 

	Examples:

	>>> pos_neg(1,-1,False)
	True 
	>>> pos_neg(1,-1,True)
	False 
	>>> pos_neg(-1,-1,True)
	True 
	>>> pos_neg(1,1,False)
	False
	>>> pos_neg(1,1,True)
	False
	""" 
	if num1<0 and num2>0 and negative==False:
		return True
	if num1>0 and num2<0 and negative==False:
		return True
	if num1<0 and num2<0 and negative==True:
		return True 
	else:
		return False
print(pos_neg(9,10,False))

