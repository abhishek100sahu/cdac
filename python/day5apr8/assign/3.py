# 3.Write a code to check the given string is palindrome or not. (abba)

s = "abba"

l = lambda a : (s == s[::-1])

print(s,"is Palindrome : ",l(s))
