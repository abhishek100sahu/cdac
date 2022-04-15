"""
3.Write a code to create a dictonary from given number range
-If the input is 4 then the keys in dictionary are 1,2,3,4
-And value is square of the key
{1:1, 2:4, 3:9 ,4:16, 5:25}
"""

x = int(input("Enter number : "))
dic = {}
a = int(1)
for i in range(0, x):
	dic[a] = a*a
	a += 1
print(dic)
