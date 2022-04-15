d = """The Internet of things describes physical objects with sensors, processing ability, software, and other technologies that connect and exchange data with other devices and systems over the Internet or other communications networks"""

d = d.split()
print("Before :")
print(d)
for i in range(1, len(d), 2):
	d[i] = d[i].upper()
print("After")
for i in range(0, len(d)):
	print(d[i])
print(" ".join(d))
