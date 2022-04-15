# sum of n odd no.s

i = int(0)
add = int(0)
while i < 101:
	if i%2 != 0:
		add += i
	i = i + 1
print(add)

# for loop for adding even no.
add = 0
for i in range(2, 101, 2):
	print(str(i), end="\t")
	add += i
print(add)

# floor division
x = int(20)
y = int(7)

print(x//y)

