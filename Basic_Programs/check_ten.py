"""
 this function is used to check the sum of two numbers is ten
 or one of them is ten 
 Author : Anmol Kumar
 Date   : 19 December 2022
 """
def check_ten(num1,num2):
	"""
	Check that sum of num1 and num2 is ten or one of them is ten

    Parameter num1 : num1 is the value given by user
    Precondition : num1  shloud be in int or float type
    Parameter num2 : num2 is the value given by user 
    Precondition :num2 should be in int or float type value

    Examples:

    >>> check_ten(5,5)
    "Sum is Ten"
    >>> check_ten(10,0)
    "One of them is ten"
    >>> check_ten(12,1)
    "Not sum and one of them is ten"
    >>> check_ten(21,-11)
    "Not sum and one of them is ten"
    """
	if num1==10 or num2==10:
		print("One of them is ten")
	elif num1+num2==10:
		print("Sum is Ten")
	else:
		print("Not sum and one of them is ten")
check_ten(22,-12)