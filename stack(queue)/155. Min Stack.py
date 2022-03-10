class MinStack:

    def __init__(self):
        self.min_num = None
        self.stack = []

    def push(self, val: int) -> None:
        if self.min_num is None:
            self.min_num = val
        else:
            if val < self.min_num:
                self.min_num = val
        self.stack.append(val)

    def pop(self) -> None:
        num = self.stack.pop()
        if num == self.min_num:
            self.min_num = sorted(self.stack)[0]
        return num

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)
