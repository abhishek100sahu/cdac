#2.Write a code to check user given interger is palindrime or not

num = int(input("Enter any number to check its palindrome or not\n"))

temp = num
rev = 0
while (num > 0):
	y = num % 10
	rev = rev * 10 + y
	num = num // 10

if temp == rev:
	print("Its a Palindrome")
else:
	print("Its not a Palindrome")
