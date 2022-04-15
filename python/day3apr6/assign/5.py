"""
5.Fruit shop project:
Implement using dictionary
	-Add fruit
	-Delete fruit by name
	-Search fruit by name and rate
	-Change fruit name and rate
	-Display
Properties: fruit_id,fruit_name,rate,imported_from,import_date,buy_price
"""
fruit = []

# Menu
def menu():
	print("""press[1]-Add fruit
press[2]-Delete fruit by name
press[3]-Search fruit by name and rate
press[4]-Change fruit name and rate
press[5]-Display
press[6]-Exit""")

# adding fruit detatils
def add():
	temp = {}
	temp["fruit_id"] = int(input("fruit_id :"))
	temp["fruit_name"] = input("fruit_name :")
	temp["rate"] = int(input("rate :"))
	temp["imported_from"] = input("imported_from :")
	temp["import_date"] = input("import_date :")
	temp["buy_price"] = int(input("buy_price :"))
	fruit.append(temp)
# deleting fruit detatils
def delete():
	f = int(input("fruit_id : "))
	for i in fruit:	
		if f == i["fruit_id"]:
			fruit.remove(i)
		else:
			print("Sorry!\n")

# search fruit
def search():
	n = input("Check fruit_name : ")
	for i in fruit:	
		if n == i["fruit_name"]:
			print(i)
		else:
			print("Sorry!\n")

# change fruit
def change():
	f = input("fruit_name :")
	for i in fruit:
		if i["fruit_name"] == f:
			i["fruit_name"] = input("fruit_name : ")
			i["rate"] = input("rate : ")
			print("Success")
		else:
			print("Sorry! fruit_name not in list")

# display fruit detatils
def display():
	print(fruit)
# Menu driven
while 1:
	menu()
	ch = int(input("Choice : "))

	if(ch == 1):
		add()
	elif(ch == 2):
		delete()
	elif(ch == 3):
		search()
	elif(ch == 4):
		change()
	elif(ch == 5):
		display()
	elif(ch == 6):
		break
	else:
		print("Invalid")
