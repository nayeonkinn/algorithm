class MyQueue:

    def __init__(self):
        self.stack = []
        self.temp = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        while len(self.stack) != 1:
            self.temp.append(self.stack.pop())
        result = self.stack.pop()
        while self.temp:
            self.stack.append(self.temp.pop())
        return result

    def peek(self) -> int:
        while self.stack:
            element = self.stack.pop()
            self.temp.append(element)
        while self.temp:
            self.stack.append(self.temp.pop())
        return element

    def empty(self) -> bool:
        return not self.stack
        

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()