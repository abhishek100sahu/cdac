"""
4.Write a code to iterate through the given string and store the alphabet and count(occurance) in dictionary
-{A:2,a:1, s:10, d:20 ,f:30}
"A computer is a machine that can be programmed to carry out sequences of
 arithmetic or logical operations automatically. Modern computers can perform
 generic sets of operations known as programs. These programs enable computers
 to perform a wide range of tasks. A computer system is a complete computer
 that includes the hardware operating system main software  and peripheral
 equipment needed and used for full operation. This term may also refer 
to a group of computers that are linked and function together"
"""

data = """A computer is a machine that can be programmed to carry out sequences of
 arithmetic or logical operations automatically. Modern computers can perform
 generic sets of operations known as programs. These programs enable computers
 to perform a wide range of tasks. A computer system is a complete computer
 that includes the hardware operating system main software  and peripheral
 equipment needed and used for full operation. This term may also refer 
to a group of computers that are linked and function together"""

c = {}
char = [65, 97, 115, 100, 102]

for i in char:
	count = 0
	char = chr(i)
	for j in range(len(data)):	
		if data[j] == char:
			count += 1
	c[char] = count
	
#print(c)
#toFind = [65, 97, 115, 100, 102]
#for i in toFind:
#	count = 0
#	convert = chr(i)
#	for j in range(len(data)):
#		if data[j] == convert:
#			count += 1
#	c[convert] = count
print(c)

