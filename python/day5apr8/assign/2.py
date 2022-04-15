"""
Use Lambda functions
num="5,2,3,9,5,6,11,8,9"
Use above string in below questions:
2.Perform addition of all even number from string
"""
num="5,2,3,9,5,6,11,8,9"
num = (num.split(","))
num = list(filter(lambda i : (int(i) % 2 == 0), num))

s = 0
add = lambda x : int(x) + s

for i in num:
	s = add(i)
print(s)
