string = input("Enter string : ")
lst = string.split(" ") # use ("") for characters
new_lst = []

for i in lst:
	if lst.count(i) == 1:
		new_lst.append(i)

l = list(filter(lambda i : lst.count(i) == 1, lst))
print(" ".join(l))
