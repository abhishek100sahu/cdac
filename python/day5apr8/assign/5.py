# 5. Write a program to generate list of numbers from 10 to 50, Use map to find square of all numbers from list

lst = list(range(10, 50))
lst1 = list(range(9))
l = list(filter(lambda x, y: (x == y * y), lst))
print(l) 0
