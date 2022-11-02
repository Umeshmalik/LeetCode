class OrderedStream:

    def __init__(self, n: int):
        self.map = [None] * n
        self.pointer = 0
        self.n = n

    def insert(self, idKey: int, value: str) -> List[str]:
        self.map[idKey-1] = value
        res = []
        while self.pointer < self.n and self.map[self.pointer]:
            res.append(self.map[self.pointer])
            self.pointer += 1
        return res


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)