# 7.Write a code to reverse every word of a paragraph

d = """The Internet of things describes physical objects with sensors, processing ability, software, and other technologies that connect and exchange data with other devices and systems over the Internet or other communications networks"""

data = d.split(" ")
print(data)
print("\n")
for i in range(0, len(data)): 
	data[i] = data[i][::-1]
print(data)
