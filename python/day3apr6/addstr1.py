num = "5,2,3,9,5,6,7,8,9"
lst = num.split(",")
print(lst)
res = 0
for i in lst:
	res += int(i)
print(res)
res = 0
for i in lst:
	if(int(i) % 2 == 0):
		res += int(i)
print(res)
