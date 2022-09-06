class MyStack:

    def __init__(self):
        self.queue = []
        self.temp = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        while len(self.queue) != 1:
            self.temp.append(self.queue.pop(0))
        result = self.queue.pop(0)
        while self.temp:
            self.queue.append(self.temp.pop(0))
        return result

    def top(self) -> int:
        while self.queue:
            element = self.queue.pop(0)
            self.temp.append(element)
        while self.temp:
            self.queue.append(self.temp.pop(0))
        return element

    def empty(self) -> bool:
        return not self.queue
        

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()