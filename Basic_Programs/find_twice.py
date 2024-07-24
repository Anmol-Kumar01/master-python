""" This program is used to find the number which occur twice.
Author : Anmol Kumar 
Date   : 24 December 2022"""
num1=int(input("Enter the first number1 "))
num2=int(input("Enter the first number2 "))
num3=int(input("Enter the first number3 "))
num4=int(input("Enter the first number4 "))
num5=int(input("Enter the first number5 "))
def twice_num(num1,num2,num3,num4,num5):
	
	if num1==num2 or num1==num3 or num1==num4 or num1==num5:
		print ("Yes there is a number which is repeated that is",num1)
	elif (num2==num3 or num2==num4 or num2==num5):
		print ("Yes there is a number which is repeated that is",num2)
	elif (num3==num4 or num3==num5):
		print ("Yes there is a number which is repeated that is",num3)
	elif (num4==num5):
		print ("Yes there is a number which is repeated that is",num4)
	else:
		print ("All numbers are unique")
twice_num(num1,num2,num3,num4,num5)