class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = [None] * k
        self.capa = k
        self.size = 0
        self.front = k - 1
        self.rear = 0

    def insertFront(self, value: int) -> bool:
        if self.size + 1 <= self.capa:
            self.deque[self.front] = value
            self.front = (self.front - 1) % self.capa
            self.size += 1
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if self.size + 1 <= self.capa:
            self.deque[self.rear] = value
            self.rear = (self.rear + 1) % self.capa
            self.size += 1
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if self.size != 0:
            self.front = (self.front + 1) % self.capa
            self.size -= 1
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        if self.size != 0:
            self.rear = (self.rear - 1) % self.capa
            self.size -= 1
            return True
        else:
            return False

    def getFront(self) -> int:
        if self.size != 0:
            return self.deque[(self.front + 1) % self.capa]
        else:
            return -1

    def getRear(self) -> int:
        if self.size != 0:
            return self.deque[(self.rear - 1) % self.capa]
        else:
            return -1

    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.size == self.capa:
            return True
        else:
            return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()