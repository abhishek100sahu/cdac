"""
Write a function in python that checks if paranthesis in the string are balanced or not. Possible parantheses are "{}',"()" or "[]". Use Stack class from the tutorial.
    - is_balanced("({a+b})")     --> True
    - is_balanced("))((a+b}{")   --> False
    - is_balanced("((a+b))")     --> True
    - is_balanced("))")          --> False
    - is_balanced("[a+b]*(x+2y)*{gg+kk}") --> True
"""

from collection_stack import Stack

def is_matched(ch1, ch2):
    brackets = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    
    return brackets[ch1] == ch2

def is_balanced(string:str):
    s1 = Stack()

    for char in string:
        if char == '(' or char == '{' or char == '[':
            s1.push(char)
        if char == ')' or char == '}' or char == ']':
            if s1.isEmpty():
                return False
            if not is_matched(char, s1.pop()):
                return False
            
    return s1.size() == 0
            
if __name__ == '__main__':
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("))"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))