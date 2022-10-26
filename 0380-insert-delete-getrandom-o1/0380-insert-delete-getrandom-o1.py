from random import choice

class RandomizedSet:

    def __init__(self):
        self.mp = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.mp: return False
        self.mp[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.mp: return False
        last_ele, idx = self.list[-1], self.mp[val]
        self.mp[last_ele], self.list[idx] = idx, last_ele
        del self.mp[val]
        self.list.pop()
        return True

    def getRandom(self) -> int:
        return choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()