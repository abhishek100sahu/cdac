# 6.Write  menu driven Student names storage system:
# ->Add student name
# ->Delete student name
# ->Check Student is present or not in list
# ->display

# ->Add student name
name = []

def add():
	
	name.append(input("Name : "))

# ->Delete student name\
def delete():
	if (check()):
		name.remove(input("Name to remove from students : "))
		print("Success!")
	else:
		print("unsuccessful!")

# ->Check Student is present or not in list
def check():
	n = input("Check name : ")
	if(n in name):
		print("name is in the list\n")
	else:
		print("name is not in the list\n")

# ->display
def display():
	print(name)

# Menu
while 1:
	ch = int(input("""press[1] ->Add student name\npress[2] ->Delete student name\npress[3] ->Check Student is present or not in list\npress[4] ->display\npress[5] ->Exit\n"""))

	if(ch == 1):
		add()
	elif(ch == 2):
		delete()
	elif(ch == 3):
		check()
	elif(ch == 4):
		display()
	elif(ch == 5):
		break
	else:
		print("Invalid")
