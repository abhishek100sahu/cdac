# 4.Write a python code to take string input from user and remove duplicate words.

string = input("Enter a paragraph : ")
string = string.split()
dic = {}
count = 0
for i in string:
	count = string.count(i)
	dic[i] = count
print(dic)
