class MinStack:

    def __init__(self):
        self.stack = []
        self.stack_mins = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.stack_mins:
            self.stack_mins.append(val)
        else:
            current_min = min(val, self.stack_mins[-1])
            self.stack_mins.append(current_min)


    def pop(self) -> None:
        self.stack.pop()
        self.stack_mins.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.stack_mins[-1]
        
