class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.mainstk = []
        self.minstk = []

    def push(self, x: int) -> None:
        if len(self.mainstk) == 0:
            self.mainstk.append(x)
            self.minstk.append(x)
        else:
            maintop = self.mainstk[-1]
            mintop = self.minstk[-1]
            if x <= mintop:
                self.mainstk.append(x)
                self.minstk.append(x)
            else:
                self.mainstk.append(x)
                self.minstk.append(mintop)

    def pop(self) -> None:
        self.mainstk.pop()
        self.minstk.pop()

    def top(self) -> int:
        return self.mainstk[-1]

    def getMin(self) -> int:
        return self.minstk[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-1)

print(minStack.mainstk)
print(minStack.minstk)

print(minStack.getMin())   #--> Returns -3.
print(minStack.top())
minStack.pop()
print(minStack.getMin())   #--> Returns -2.
