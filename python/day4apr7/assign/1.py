"""
Use Class-Object
1.Start a mini project Console ERP system.
	-Add Employee
	-Delete Employee
	-Search Employee by name
	-Search employee by empid
	-Search employee by salary(Check greater)
	-Change Employee Data(name,id,salary)
	-Display
Empid, Name,age,gender,place,salary,previous_company,joining_date 
"""
class ERP:
	def __init__(self,Empid = 0, Name = "",age = 0,gender = "",place = "",salary = 0,previous_company = "",joining_date = ""):
		self.Empid = Empid
		self.Name = Name
		self.age = age
		self.gender = gender
		self.place = place
		self.salary = salary
		self.previous_company = previous_company
		self.joining_date = joining_date

	def display(self):
		print("\nEmpid",self.Empid)
		print("Name",self.Name)
		print("age",self.age)
		print("gender",self.gender)
		print("place",self.place)
		print("salary",self.salary)
		print("previous_company",self.previous_company)
		print("joining_date",self.joining_date)
		print("\n")

ERP_list = []

# add
def add():
	Empid = int(input("Empid : "))
	Name = input("Name : ")
	age = int(input("age : "))
	gender = input("gender : ")
	place = input("place : ")
	salary = int(input("salary : "))
	previous_company =input("previous_company : ")
	joining_date = input("joining_date : ")
	e = ERP(Empid,Name,age,gender,place,salary,previous_company,joining_date)
	ERP_list.append(e)

# delete
def delete():
	empid = int(input("Enter id to delete : "))
	for i in ERP_list:
		if empid == i.Empid:
			ERP_list.remove(i)
			print("Deleted Successfully.")
# Display
def dis():
	for i in ERP_list:
		i.display()

# Search by id
def search():
	empid = int(input("empid to search : "))
	for i in ERP_list:
		if empid == i.Empid:
			i.display()

# Search by name
def search_by_name():
	emp_name = (input("Employee name to search : "))
	for i in ERP_list:
		if emp_name == i.Name:
			i.display()

# Change data
def change_data():
	empid = int(input("Enter empid to change data : "))
	for i in ERP_list:
		if empid == i.Empid:
			i.Empid = input("Empid : ")
			i.Name = input("Name : ")	
			i.salary = int(input("salary : "))
			print("Updated successfully.")

# Search employee by salary greater than
def sal():
	emp_salary = int(input("Enter salary : "))
	for i in ERP_list:
		if emp_salary <= i.salary:
			print("\nEmployees having salary greater than entered value :\n")
			i.display()
# Dictionary of menu
menu = {
	"1" : add,
	"2" : delete,
	"3" : dis,
	"4" : search,
	"5" : search_by_name,
	"6" : change_data,
	"7" : sal
}

while True:
	print("[1]Add\n[2]delete\n[3]display\n[4]Search by id\n[5]Search by name\n[6]Change data\n[7]Search employee by salary range\n[8]Exit")
	ch = input("Enter choice :")

	if ch == "8":
		break

	print(menu[ch]())

