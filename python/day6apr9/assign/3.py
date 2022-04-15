string = """A computer is a machine that can be programmed to carry out sequences of arithmetic or logical operations automatically. Modern computers can perform generic sets of operations known as programs. These programs enable computers to perform a wide range of tasks. A computer system is a complete computer that includes the hardware operating system main software  and peripheral equipment needed and used for full operation. This term may also refer  to a group of computers that are linked and function together"""

"""
3.Write the above string into 10 files data3.txt,data4.txt and so on.. 
"""

for i in range(3,14):
	fd = open(f"data{i}.txt","w+")
	for j in string:	
		fd.write(j)
