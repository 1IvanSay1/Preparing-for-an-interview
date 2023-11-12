class Stack:

    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0
    
    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)
    
def is_balanced(s):
    stack = Stack()
    for char in s:
        if char in "([{":
            stack.push(char)
        else:
            if stack.is_empty():
                return False
            last_open = stack.pop()
            if (last_open, char) not in [("(", ")"), ("[", "]"), ("{", "}")]:
                return False
    return stack.is_empty()


if __name__ == '__main__':
    stack = '(((([{}]))))'
    if is_balanced(stack):
        print("Сбалансированно")
    else:
        print("Несбалансированно")  
    X = Stack()
    X.push()
    X.peek()
    X.size()
    X.pop()
    X.is_empty()
    X.cb()
