""" This Program is used to determined the sign of given numbers 
Author : Anmol Kumar
Date   : 18 December 2022 """
def sign(num1,num2):
	""" Return True if sign of num1 is same as num2 otherwise False

	    Parameter num1 : num1 is a number given by user
	    Precondition num1: num1 is only numeric type value
	    Parameter num2 : num2 is a number given by user
	    Precondition num2: num2 is only numeric type value

	    examples:
	    >>> sign(22,33)
	    True
	    >>> sign(-4,-3)
	    True
	    >>> sign(-4,9)
	    False """
	    
	if num1>=0 and num2>=0 or num1<0 and num2<0:
		# print ("True")
		return True
	# elif num1==0 and num2==0:
	# 	return True
	elif (num1==0 and (num2>0 or num2<0)) or (num2==0 and(num1>0 or num2<0)):
		#print ("False")
		return False
	else:
		#print("False")
		return False
	
num1=int(input("Enter the num1 "))
num2=int(input("Enter the num2 "))
a=sign(num1,num2)
print (a)