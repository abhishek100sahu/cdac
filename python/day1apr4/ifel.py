#greater number program

a=int(input("Enter num1 :\n"))
b=int(input("Enter num2 :\n"))
c=int(input("Enter num3 :\n"))

if(a>b):
	if(a>c):
		print("num1 is greater")
	else:
		print("num3 is greater")
else:
	if(b>c):
		print("num2 is greater")
	else:
		print("num3 is greater")
#_______________________________________
if(a>b and a>c):
	print("num1 is greater")
else:
	print("num1 is not greater")

if(a>b or a>c):
	print("num1 is greater than num2 or num3")
#_________________________________________________

