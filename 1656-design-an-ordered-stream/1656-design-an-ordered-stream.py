class OrderedStream:

    def __init__(self, n: int):
        self.arr = [None] * n
        self.pointer = 0
        self.n = n

    def insert(self, idKey: int, value: str) -> List[str]:
        self.arr[idKey-1] = value
        res = []
        curr = self.pointer
        while curr < self.n and self.arr[curr]:
            res.append(self.arr[curr])
            curr += 1
        self.pointer = curr
        return res


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)