string = """A computer is a machine that can be programmed to carry out sequences of
 arithmetic or logical operations automatically. Modern computers can perform
 generic sets of operations known as programs. These programs enable computers
 to perform a wide range of tasks. A computer system is a complete computer
 that includes the hardware operating system main software  and peripheral
 equipment needed and used for full operation. This term may also refer 
to a group of computers that are linked and function together"""

def change_upper(i):
	if lst.index(i) % 2 == 0:
		return i.upper()
	else:
		return i
print(" ".join(list(map(lambda i : change_upper(i), string.split(" ")))))
