"""
Projects Assignment:
1.Console ERP project
Implement using dictionary:
	-Add Employee
	-Delete Employee
	-Search Employee by name
	-Change Employee Data
		=>Change name
		=>change age
		=>Change gender
		=>change salary
	-Manage All Teams
		-Create new Team
		-Display team
		-Manage Team(Particular Team)
			-Rename Team(optional)
			-Display Members
			-Add Members
			-Delete Members
		-Delete Team
	-Display 

Properties:Empid, Name,age,gender,place,salary,previous_company,joining_date
Date format "21/04/2021" dd/mm/yyyy
"""
dic = {}
team = {}

# Menu
def menu():
	print("[1]add employee\n[2]delete employee\n[3]search employee\n[4]change employee data\n[5]teams\n[6]display employee\n[7]add team\n[8]display team\n[9]exit\n")

# Adding employee details	
def add():
	dic1 = {}
	dic1["empId"] = input("Enter empId :")
	dic1["name"] = input("Enter name : ")
	dic1["age"] = input("Enter age : ")
	dic1["gender"] = input("Enter gender : ")
	dic1["place"] = input("Enter place : ")
	dic1["salary"] = input("Enter salary : ")
	dic1["previous_company"] = input("Enter previous_company : ")
	print("Enter joining_date")
	x = (input("Enter month : "))
	y = (input("Enter date : "))
	z = (input("Enter year : "))
	date = "/".join([x,y,z])

	dic1["joining_date"] = date
	dic[dic1["empId"]] = dic1

# Deleting Employee details
def delete():
	f = input("empId : ")

	for i in list(dic.keys()):
		if f == i:
			del dic[str(i)]
			print("success")
		else:
			print("not found")
 
# Searching Employee details via empId
def search():
	f = input("empId to find : ")
	for i in list(dic.keys()):
		if f == i:
			if dic[str(i)]["empId"] == f:
				print("\nfound\n")
			else:
				print("\nnot found\n")

# Changing Employee details
def change():
	chn = int(input("[1] change name\n[2] change age\n[3] change gender\n[4] change salary"))
	if chn == 1:
		f = input("Enter empId : ")
		name = input("Enter name to change : ")
		for i in list(dic.keys()):
			if f == i:
				dic[i]["name"] = name
				print("Success")
	if chn == 2:
		f = input("Enter empId : ")
		age = input("Enter age to change : ")
		for i in list(dic.keys()):
			if f == i:
				dic[i]["age"] = age
				print("Success")
	elif chn == 3:
		f = input("Enter empId : ")
		gender = input("Enter gender to change : ")
		for i in list(dic.keys()):
			if f == i:
				dic[i]["gender"] = gender
				print("Success")
	elif chn == 4:
		f = input("Enter empId : ")
		salary = input("Enter salary to change : ")
		for i in list(dic.keys()):
			if f == i:
				dic[i]["salary"] = salary
				print("Success")
	else:
		print("Sorry!")
# Displaying Employee details
def display():
	for i in list(dic.keys()):
		print(dic[i])

# Adding Employee in team
def add_team():
	team1 = {}
	team1["teamId"] = input("Enter teamId : ")
	team1["teamName"] = input("Enter project_name : ")
	empId = input("Enter empId of employee to add in team : ")
	for i in list(dic.keys()):
		if empId == i:
			empId = list(map(lambda x : x, dic[i]))
			team["member"] = empId			
			print("Success!")
	team[team1["teamId"]] = team1.items()
		

# Display team members
def display_team():
	#for i in list(team.keys()):
	print(team)
while 1:
	menu()
	ch = int(input("Choice : "))
	
	if ch == 1:
		add()
	elif ch == 2:
		delete()
	elif ch == 3:
		search()
	elif ch == 4:
		change()
	elif ch == 5:
		team()
	elif ch == 6:
		display()
	elif ch == 7:
		add_team()
	elif ch == 8:
		display_team()
	elif ch == 9:
		break



















