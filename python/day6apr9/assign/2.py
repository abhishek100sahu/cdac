string = """A computer is a machine that can be programmed to carry out sequences of arithmetic or logical operations automatically. Modern computers can perform generic sets of operations known as programs. These programs enable computers to perform a wide range of tasks. A computer system is a complete computer that includes the hardware operating system main software  and peripheral equipment needed and used for full operation. This term may also refer  to a group of computers that are linked and function together"""

"""
2.Write the above string alternate index words into the file data2.txt
"""

fd = open("data2.txt", "r+")
lst = string.split(" ")
lst1 =" ".join(list(filter(lambda i : lst.index(i) % 2 == 0, lst)))
print(lst1)
for i in lst1:
	fd.write(i)
print(fd.read())
