class Stack:

    def __init__(self):
        self.store = []

    def push(self, elem):
        self.store.append(elem)
    
    def pop(self):
        store_len = len(self.store)
        if store_len == 0:
            return None
        return self.store.pop(len(self.store) - 1)
    
    def peek(self):
        store_len = len(self.store)
        if store_len == 0:
            return None
        return self.store[len(self.store) - 1]
    
    def is_empty(self):
        return len(self.store) == 0

class Solution:
    def isValid(self, s: str) -> bool:
        op = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        stack = Stack()
        for b in s:
            if b in op:
                stack.push(op[b])
            else:
                o = stack.pop()
                if o is None:
                    return False
                if o != b:
                    return False
        return stack.is_empty()

