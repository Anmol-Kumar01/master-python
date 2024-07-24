'''This program is used to find the target number.
Author : Anmol Kumar
Date   : 25 December 2022'''
target_num=int(input("Please enter the target number "))
num1=int(input("Please enter the num1  "))
num2=int(input("Please enter the target num2 "))
num3=int(input("Please enter the target num3 "))
def target_num1(num1,num2,num3):
	"""Returns : true if any two of them num1,num2 or num3 sum up to give the target number otherwise false
	if (num1 + num2 == target_num or num1 + num3 == target_num) or (num2 + num3 == target_num):
		return True
	else:
		return False
print(target_num1(num1,num2,num3))