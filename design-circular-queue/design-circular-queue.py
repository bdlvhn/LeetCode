class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = collections.deque()
        self.k = k

    def enQueue(self, value: int) -> bool:
        if len(self.queue) == self.k:
            return False
        else:
            self.queue.append(value)
            for i in range(len(self.queue) - 1):
                self.queue.append(self.queue.popleft())
            return True
    
    def deQueue(self) -> bool:
        if not self.queue:
            return False
        else:
            self.queue.pop()
            return True
            
    def Front(self) -> int:
        if not self.queue:
            return -1
        else:
            return self.queue[-1]
        
    def Rear(self) -> int:
        if not self.queue:
            return -1
        else:
            return self.queue[0]
    
    def isEmpty(self) -> bool:
        return not self.queue
    
    def isFull(self) -> bool:
        return len(self.queue) == self.k