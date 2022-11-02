class CustomStack:

    def __init__(self, maxSize: int):
        self.size = maxSize
        self.stack = []
        self.currSize = 0

    def push(self, x: int) -> None:
        if self.currSize == self.size: return
        self.stack.append(x)
        self.currSize += 1

    def pop(self) -> int:
        if self.currSize == 0: return -1
        self.currSize -= 1
        return self.stack.pop()        
        
    def increment(self, k: int, val: int) -> None:
        i = 0
        while i < self.currSize and i < k:
            self.stack[i] += val
            i += 1

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)