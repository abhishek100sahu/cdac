"""
Write a function in python that can reverse a string using stack data structure. Use Stack class from the tutorial.

    - reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"
"""

from collection_stack import Stack

stack_obj = Stack()

string1 = "We will conquere COVID-19"

for char in string1:
    stack_obj.push(char)

reversed_string1= str()
    
while stack_obj.size() != 0:
    reversed_string1 += stack_obj.pop()
    
print(reversed_string1)