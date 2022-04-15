num1 = int(input("Enter number1 :"))
num2 = int(input("Enter number2 :"))
num3 = int(input("Enter number3 :"))
num4 = int(input("Enter number4 :"))

if(num1 > num2 and num1 > num3 and num1 > num4):
	print("number1 is the greatest")
elif(num2 > num1 and num2 > num3 and num2 > num4):
	print("number2 is the greatest")
elif(num3 > num1 and num3 > num2 and num3 > num4):
	print("number3 is the greatest")
elif(num4 > num1 and num4 > num2 and num4 > num3):
	print("number4 is the greatest")
else:
	print("Invalid")
