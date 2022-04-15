data="""The internet of things, or IoT, is a system of interrelated computing devices, mechanical and digital machines, objects, animals or people that are provided with unique identifiers (UIDs) and the ability to transfer data over a network without requiring human-to-human or human-to-computer interaction."""

str1 = input("{} \n\nEnter sub string\n".format(data))
x = data.find("{}".format(str1))
if(x != -1):
	print("String matched")
str2 = str1[:5]
str2 = str2.upper()
print("{}{}".format(str2, str1[5:]))
temp = data[x:x+6]
print(temp.upper)
