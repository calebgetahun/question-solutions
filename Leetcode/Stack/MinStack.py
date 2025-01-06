class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')
        
    def push(self, val: int) -> None:
        if self.stack:
            curr_min = self.stack[-1][1]
            if val < curr_min:
                self.stack.append((val, val))
                self.min = val
            else:
                self.stack.append((val, curr_min))
        else:
            self.stack.append((val, val))
            self.min = val

    def pop(self) -> None:
        popped = self.stack.pop()
        if self.stack:
            if popped[1] < self.stack[-1][1]:
                self.min = self.stack[-1][1]
        else:
            self.min = float('inf')      

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

if __name__ == "__main__":
    min_stack = MinStack()
    min_stack.push(8)
    print(min_stack.top())
    min_stack.push(6)
    print(min_stack.getMin())
    min_stack.pop()
    print(min_stack.getMin())

# TC: O(1) for push, pop, top, and getMin operations
# SC: O(N) to hold stack element minimum pairs as well as the actual minimum