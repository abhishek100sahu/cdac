print("[1]Add")
print("[2]Sub")
print("[3]Mul")
print("[4]Div")

ch = int(input("Enter choice : "))
a = int(input("a :"))
b = int(input("b :"))

if(ch == 1):
	print(a + b)
elif(ch == 2):
	print(a - b)
elif(ch == 3):
	print(a * b)
elif(ch == 4):
	print(a / b)
else:
	print("Invalid")
	
