num = "5, 2, 3, 9 ,5 ,6 ,7 ,8 ,9"
num = num.replace(",", "")
num = num.replace(" ", "")

print(num)
s = 0
for i in num:
	n = int(i)
	s += n
print(s) 
