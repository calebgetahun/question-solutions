class MyQueue:
    def __init__(self):
        self.stack_one = []
        self.stack_two = []        

    def push(self, x: int) -> None:
        self.stack_one.append(x)

    def pop(self) -> int:
        if self.stack_two:
            return self.stack_two.pop()
        while self.stack_one:
            temp = self.stack_one.pop()
            self.stack_two.append(temp)
        return self.stack_two.pop()
    
    def peek(self) -> int:
        if self.stack_two:
            return self.stack_two[-1]
        elif self.stack_one:
            return self.stack_one[0] 
        else:
            return -1
    
    def empty(self) -> bool:
        if not self.stack_one and not self.stack_two:
            return True
        return False
        
if __name__ == "__main__":
    q = MyQueue()
    q.push(5)
    q.push(6)
    q.push(7)
    ans = []
    param_2 = q.pop()
    ans.append(param_2)
    param_3 = q.peek()
    ans.append(param_3)
    param_4 = q.empty()
    ans.append(param_4)

    print(ans)

# TC: O(1) For Push, O(1) For Peek, O(1) Amortized For Pop, O(1) For Empty
# SC: O(N) where N is the amount of 