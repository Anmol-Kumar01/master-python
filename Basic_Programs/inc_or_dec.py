"""
Author : Anmol Kumar
Date   : 24 December 2022"""
x = int(input("Enter the number "))
def operatin_num(x) :
    """
    Returns double the number and add one to it if number is even otherwise subtract one from it and double it

    Parameter x : x is a value that is gievn by user 
    Precondition: x shlould be numeric type value

    examples:
    >>> operatin_num(4)
    9
    >>> operatin_num(9)
    16
    >>> operatin_num(0)
    1
    >>> operatin_num(-10)
    -19
    """
    if x % 2 == 0 :
    	  return (x * 2) + 1
    else:
    	  return (x - 1) * 2
print(operatin_num(x))
	

	

