"""This function is used to convert the temperture given in celcius into temperature in fahrenheit.
Author : Anmol Kumar 
"""
temp1 = float(input("temp in celcius "))
def cel_to_fahn(temp1):
	""" Convert the temperature celcius into fahrenheit and give status of it 
	Parameter temp1 : temp1 is the temperature given by user in celcius 
	Precondition    : temp1 is numeric type value.

	examples:
	>>> cel_to_fahn(37)
	98.6
	Hot
	>>> cel_to_fahn(-40)
	-40.0
	cold
	>>> cel_to_fahn(20)
	68.0
	fair"""
	x = (temp1*9/5)+32
	print(x)
	if x<=60:
		print("cold")
	if 60<x<=85:
		print("fair")
	elif x>85:
		print("Hot")
cel_to_fahn(temp1)
	

