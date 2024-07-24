x= 2#float(input("Enter the first Number "))
y= 1#float(input("Enter the second Number ")) 
def add(x,y):
	a= x + y 
	b= x * y 
	c= x / y 
	d= x - y
	#print("Addition is ",a,"multiplication is",b,"Division is",c,"Subtraction is",d)
	print(f'Addition is {a} multiplication is {b} Division is {c} Subtraction is {d}')
add(x,y)