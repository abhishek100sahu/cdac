months = ['Jan', 'Feb', 'March', 'Apr', 'May', 'June', 'July',
          'Aug', 'Sept', 'Oct', 'Nov', 'Dec']

x = (input("Enter Date (mm/dd/yyyy): "))
mon, date, year = x.split('/')
mon = months[int(mon)-1]
print(f"Formatted Date (Mm dd, yyyy): {mon} {date}, {year}")
