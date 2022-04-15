i = 1
while i <= 10:
	print(i*2)
	i += 1
print("For loop")
for i in range(1, 11):
	print(i*3)

print("vene number till 20")
for x in range(1, 21):
	if(x % 2 == 0):
		print(x, "is even")
print("_"*50)
print("a"*10)
print("a"+'b')
print("abcd 'xyz'cc")
# invalid print('abcd 'xyz'cc')
pi = str(3.14)# this'll be printed 3.14
print(pi)

# invalid a = int('sid')
# print(a)
a = int("1000000000000000000000000000000000000000000000000000000")# this'll be integer
print(type(a))
