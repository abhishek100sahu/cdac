"""
Use Lambda functions
num="5,2,3,9,5,6,11,8,9"
Use above string in below questions:
1.Perform addition of all numbers in the string
"""
num = "5,2,3,9,5,6,11,8,9"

num = (num.split(","))
s = 0
add = lambda x : int(x) + s
for i in num:
	s = add(i)
print(s)
