class OrderedStream:

    def __init__(self, n: int):
        self.map = {}
        self.pointer = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.map[idKey-1] = value
        res = []
        while self.pointer in self.map:
            res.append(self.map[self.pointer])
            self.pointer += 1
        return res


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)