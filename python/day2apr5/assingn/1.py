#1.Write code to check string is palindrome or not

str = str(input("Enter any string to check its palindrome or not\n"))

if str[:] == str[::-1]:
    print("Its a Palindrome")
else:
    print("Its not a Palindrome")
