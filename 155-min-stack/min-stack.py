class MinStack:
    def __init__(self):
        self.stack = []
        self.index = -1 

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.index += 1

    def pop(self) -> None:
        if self.index == -1:
            return None
        val = self.stack.pop()
        self.index -= 1
        return val

    def top(self) -> int:   # now safe to use this method name
        if self.index == -1:
            return None
        return self.stack[self.index]

    def getMin(self) -> int:
        if self.index == -1:
            return None
        return min(self.stack)
