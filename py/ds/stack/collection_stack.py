from collections import deque

class Stack:
    
    def __init__(self) -> None:
        self.container = deque()
    
    
    def push(self, value):
        self.container.append(value)
    
    
    def pop(self):
        return self.container.pop()
    
    
    def isEmpty(self):
        return len(self.container) == 0
    
    
    def peek(self):
        return self.container[-1]
    
    
    def size(self) -> int:
        return len(self.container)
    

if __name__ == '__main__':
    s1 = Stack()

    s1.push(234)
    s1.push(4)
    s1.push(654)
    s1.push(8884)
    s1.pop()
    print(s1.peek())
    print(s1.container)