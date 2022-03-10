class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.peek = None

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        num = self.stack2.pop()
        self.peek = self.stack2.pop()
        self.stack1.append(self.peek)
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return num

    def peek(self) -> int:
        return self.peek

    def empty(self) -> bool:
        if len(self.stack1) == 0:
            return True
        return False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
