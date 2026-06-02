class MinStack:

    def __init__(self):
        self.store = []
        self.mins = []
        

    def push(self, val: int) -> None:
        if len(self.mins) == 0:
            print(f"First min: {val}")
            self.mins.append(val)
        elif self.mins[len(self.mins) - 1] >= val:
            print(f"New min: {val}")
            self.mins.append(val)
        self.store.append(val) 

    def pop(self) -> None:
        if len(self.store) == 0:
            return
        popped = self.store.pop() 
        if popped == self.mins[len(self.mins) - 1]:
            self.mins.pop()

    def top(self) -> int:
        if len(self.store) == 0:
            return None
        return self.store[len(self.store) - 1]
        

    def getMin(self) -> int:
        if len(self.store) == 0:
            return None
        return self.mins[len(self.mins) - 1]
        
