def sum_double(num1,num2):
	"""Returns : twice the sum of numbers when they are same otherwise sum them.

	Parameter num1: num1 is the first number
	Precondition  : num1 is numeric type value int or float
	Parameter num2: num2 is the second number 
	Precondition  : num2 is the numeric type value int or float

	examples:
	>>> sum_double(2,2)
	8
	>>> sum_double(2.2,2.2)
	8.8
	>>> sum_double(2,5)
	7
	"""
	if num1==num2:
		return 2*(num1 + num2)
	else:
		return num1+num2
print(sum_double(2,2))

