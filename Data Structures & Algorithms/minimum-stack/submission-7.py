class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = []
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.minimum.append(val)
            return
        self.minimum.append(min(self.minimum[-1],val))
        self.stack.append(val)

    def pop(self) -> None:
        if not self.stack:
            raise IndexError("Index out of bounds")
        self.stack.pop()
        self.minimum.pop()

    def top(self) -> int:
        if not self.stack:
            raise IndexError("Index out of bounds")
        return self.stack[-1]
        

    def getMin(self) -> int:
        if not self.stack:
            raise IndexError("Index out of bounds")
        return self.minimum[-1]

