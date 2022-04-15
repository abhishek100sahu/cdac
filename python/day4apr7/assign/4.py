import math

"""
4.Define a class named Rectangle which can be constructed by a length 
and width. The Rectangle class has a method which can compute the area.
-Implement + operation (Perform addition of length and width)
-Implement documentation attribute(__doc__ attribute)
-Implement string typecasting and print "The length is ..value.. and width is ..value.."(__str__)
-Implement > operation(__gt__(self,other) and return true or false if area is greater or smaller)
-Implement == operation(__eq__(self,other) and return true or false if area is equal or not)
"""

class Rectangle:
	def __init__(self, length=1, breadth=1):
		self.length = length
		self.breadth = breadth

	def __str__(self, length=1, breadth=1):	
		return "Area of rectangle : "+str(self.length * self.breadth)

	def area(self):
		return self.length*self.breadth
	
	def __add__(self, length=1, breadth=1):
		return "Addition : "+(self.length + self.breadth)

	def __doc__(self, length=1):
		return "Assign : "+(self)

	def __gt__(self, length=1):
		return "True"

a = 23
b = 20
c = a + b
d = a
r = Rectangle(a)
s = Rectangle(b)
print(r>s)
