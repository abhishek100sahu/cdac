"""
1.Write a menu driven code to store employee information in dictionary(Only one employee details)
->Add employee details
->delete emplpoyee
->Display employee
Take input from user
Properties: Name,Age,Gender,Place,Salary,Previous_company
"""

emp = []
# menu
def menu():
	print("""
		press[1] : add
		press[2] : delete
		press[3] : display
		press[4] : exit
""")
# adding members
def add():
	temp = {}
	temp["name"] = input("name : ")
	temp["age"] = input("age : ")
	temp["gender"] = input("gender : ")
	temp["place"] = input("place : ")
	temp["salary"] = input("salary : ")
	temp["previous_company"] = input("previous_company : ")

	emp.append(temp)

# deleting members
def delete():
	ch = (input("name to delete :"))
	for i in emp:
		if i["name"] == ch:
			emp.remove(i)

# display
def display():
	print(emp)

while 1:
	menu()
	but = int(input("Choice : "))
	if but == 1:
		add()
	elif but == 2:
		delete()
	elif but == 3:
		display()
	elif but == 4:
		break
	else:
		print("Invalid")
